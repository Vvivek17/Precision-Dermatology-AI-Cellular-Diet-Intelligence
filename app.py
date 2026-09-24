"""
DermAI 360 - Flask Web Server & Clinical REST API
Serves interactive dermatology dashboard and clinical diagnostic endpoints.
"""

import os
import sys
import json
import base64
import io
from pathlib import Path
import time

# Fix Windows console UTF-8 output encoding if possible
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from flask import Flask, request, jsonify, render_template, send_from_directory, abort
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__, template_folder='.')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['UPLOAD_FOLDER'] = 'uploads'
SAMPLE_DIR = os.path.join('data', 'HAM10000', 'images')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp'}

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
    return response

@app.route('/api/<path:subpath>', methods=['OPTIONS'])
def handle_options(subpath):
    return '', 204

# ── Load model (optional) ─────────────────────────────────
MODEL = None
MODEL_PATH = os.path.join('models', 'saved', 'skin_model.keras')

def load_model():
    global MODEL
    if os.path.exists(MODEL_PATH):
        try:
            import tensorflow as tf
            MODEL = tf.keras.models.load_model(MODEL_PATH)
            print(f"[+] Model loaded from {MODEL_PATH}")
        except Exception as e:
            print(f"[!] Could not load model: {e}")
            print("    Running in intelligent simulation mode.")
    else:
        print("[i] No saved model found. Running in intelligent simulation mode.")
        print("    Train first: python train.py")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Benchmark sample images mapped to diseases
BENCHMARK_SAMPLES = [
    {
        "filename": "ISIC_0000004.jpg",
        "code": "mel",
        "name": "Melanoma",
        "severity": "Critical",
        "color": "#C0392B",
        "badge": "Critical Risk",
        "hint": "Irregular pigment network, asymmetrical border"
    },
    {
        "filename": "ISIC_0000001.jpg",
        "code": "bcc",
        "name": "Basal Cell Carcinoma",
        "severity": "High",
        "color": "#FF3366",
        "badge": "High Risk",
        "hint": "Translucent nodule, arborizing telangiectasia"
    },
    {
        "filename": "ISIC_0000000.jpg",
        "code": "akiec",
        "name": "Actinic Keratosis",
        "severity": "High",
        "color": "#FF6B35",
        "badge": "High Risk",
        "hint": "Rough scaly erythematous sun-damaged lesion"
    },
    {
        "filename": "ISIC_0000006.jpg",
        "code": "vasc",
        "name": "Vascular Lesion",
        "severity": "Medium",
        "color": "#8E44AD",
        "badge": "Medium Risk",
        "hint": "Red-purple vascular lacunae, angiomatous"
    },
    {
        "filename": "ISIC_0000005.jpg",
        "code": "nv",
        "name": "Melanocytic Nevus",
        "severity": "Low",
        "color": "#27AE60",
        "badge": "Benign",
        "hint": "Symmetric common pigment mole with regular edges"
    },
    {
        "filename": "ISIC_0000002.jpg",
        "code": "bkl",
        "name": "Benign Keratosis",
        "severity": "Low",
        "color": "#4ECDC4",
        "badge": "Benign",
        "hint": "Stuck-on waxy seborrheic keratosis"
    },
    {
        "filename": "ISIC_0000003.jpg",
        "code": "df",
        "name": "Dermatofibroma",
        "severity": "Low",
        "color": "#45B7D1",
        "badge": "Benign",
        "hint": "Firm fibrotic dermal nodule, central scar"
    },
    {
        "filename": "SAMPLE_acne.jpg",
        "code": "acne",
        "name": "Acne Vulgaris",
        "severity": "Low",
        "color": "#E67E22",
        "badge": "Common Condition",
        "hint": "Inflammatory papules, pustules, comedones & follicular plugging"
    },
    {
        "filename": "SAMPLE_ecz.jpg",
        "code": "ecz",
        "name": "Atopic Dermatitis / Eczema",
        "severity": "Medium",
        "color": "#16A085",
        "badge": "Chronic Inflammatory",
        "hint": "Pruritic erythematous patches, excoriation & skin barrier disruption"
    },
    {
        "filename": "SAMPLE_psor.jpg",
        "code": "psor",
        "name": "Plaque Psoriasis",
        "severity": "Medium",
        "color": "#D35400",
        "badge": "Autoimmune Condition",
        "hint": "Silvery micaceous scales, well-demarcated salmon plaques & Auspitz sign"
    },
    {
        "filename": "SAMPLE_vit.jpg",
        "code": "vit",
        "name": "Vitiligo",
        "severity": "Low",
        "color": "#2980B9",
        "badge": "Autoimmune Pigmentary",
        "hint": "Chalk-white depigmented macules with clear margins & trichrome sign"
    },
    {
        "filename": "SAMPLE_ros.jpg",
        "code": "ros",
        "name": "Rosacea",
        "severity": "Low",
        "color": "#C0392B",
        "badge": "Vascular Reactivity",
        "hint": "Facial centrofacial erythema, flushing, telangiectasia & inflammatory papules"
    }
]


# ── Routes ────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/diet_translations.js')
def serve_diet_translations():
    return send_from_directory('.', 'diet_translations.js', mimetype='application/javascript')


@app.route('/api/samples', methods=['GET'])
def get_samples():
    """Return benchmark lesion samples for instant one-click testing."""
    samples = []
    for item in BENCHMARK_SAMPLES:
        file_path = os.path.join(SAMPLE_DIR, item['filename'])
        exists = os.path.exists(file_path)
        samples.append({
            **item,
            "url": f"/api/sample-image/{item['filename']}",
            "available": exists
        })
    return jsonify({"success": True, "samples": samples})


@app.route('/api/sample-image/<filename>', methods=['GET'])
def get_sample_image(filename):
    """Serve sample lesion image safely."""
    safe_name = secure_filename(filename)
    if not os.path.exists(os.path.join(SAMPLE_DIR, safe_name)):
        abort(404)
    return send_from_directory(SAMPLE_DIR, safe_name, max_age=86400)


@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle image upload (base64, multipart, or sample reference) and return full prediction."""
    from models.skin_disease_model import predict_disease

    # 1. Handle JSON input (base64 or sample filename)
    if request.is_json:
        data = request.get_json(silent=True) or {}

        # Case A: Preset sample image or local file path selected
        sample_name = data.get('sample_filename') or data.get('image_path')
        if sample_name:
            safe_name = os.path.basename(sample_name)
            sample_path = os.path.join(SAMPLE_DIR, safe_name)
            if not os.path.exists(sample_path) and os.path.exists(sample_name):
                sample_path = sample_name
            if os.path.exists(sample_path):
                try:
                    result = predict_disease(sample_path, MODEL)
                    return jsonify({'success': True, 'result': result})
                except Exception as e:
                    return jsonify({'error': f"Inference failed: {str(e)}"}), 500
            else:
                return jsonify({'error': f"Specimen image '{sample_name}' not found"}), 404

        # Case B: Direct URL download
        image_url = data.get('image_url', '')
        if image_url and (image_url.startswith('http://') or image_url.startswith('https://')):
            try:
                import urllib.request
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                tmp_path = os.path.join(app.config['UPLOAD_FOLDER'], f'url_upload_{int(time.time())}.jpg')
                req = urllib.request.Request(image_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req, timeout=10) as resp, open(tmp_path, 'wb') as out_f:
                    out_f.write(resp.read())
                result = predict_disease(tmp_path, MODEL)
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                return jsonify({'success': True, 'result': result})
            except Exception as e:
                return jsonify({'error': f"Failed to download/process URL: {str(e)}"}), 500

        # Case C: Base64 data URL
        image_data = data.get('image_data', '')
        if image_data:
            try:
                if ',' in image_data:
                    header, encoded = image_data.split(',', 1)
                else:
                    encoded = image_data
                img_bytes = base64.b64decode(encoded)
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                tmp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'tmp_upload.jpg')
                with open(tmp_path, 'wb') as f:
                    f.write(img_bytes)
                result = predict_disease(tmp_path, MODEL)
                if os.path.exists(tmp_path):
                    os.remove(tmp_path)
                return jsonify({'success': True, 'result': result})
            except Exception as e:
                return jsonify({'error': str(e)}), 500

    # 2. Handle multipart file upload
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided. Upload a file or select a demo sample.'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Invalid file type. Supported formats: PNG, JPG, JPEG, WEBP'}), 400

    try:
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        result = predict_disease(filepath, MODEL)

        if os.path.exists(filepath):
            os.remove(filepath)

        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500


@app.route('/api/diseases', methods=['GET'])
def get_diseases():
    """Return all detectable skin diseases with clinical profiles and diet plans."""
    from models.skin_disease_model import DISEASE_CLASSES
    return jsonify({'success': True, 'diseases': DISEASE_CLASSES})


@app.route('/api/diet/<condition>', methods=['GET'])
def get_diet(condition):
    """Return targeted diet plan for a specific disease code or name."""
    from models.skin_disease_model import DISEASE_CLASSES
    cond_lower = condition.lower()
    for d in DISEASE_CLASSES.values():
        if d['code'].lower() == cond_lower or d['name'].lower().replace(' ', '-') == cond_lower:
            return jsonify({
                'success': True,
                'disease': d['name'],
                'code': d['code'],
                'diet_plan': d.get('diet_plan', {})
            })
    return jsonify({'error': f'Disease condition "{condition}" not found'}), 404


@app.route('/api/diet/<condition>/cultural', methods=['GET'])
def get_cultural_diet_endpoint(condition):
    """Return culturally-tailored 3-meal split for a specific country, preference, and language."""
    from models.cultural_diets import get_cultural_diet_plan, SUPPORTED_COUNTRIES, SUPPORTED_LANGUAGES
    country = request.args.get('country', 'india')
    preference = request.args.get('preference', 'non_veg')
    lang = request.args.get('lang', 'en')
    
    plan = get_cultural_diet_plan(condition, country=country, preference=preference, lang=lang)
    return jsonify({
        'success': True,
        'cultural_plan': plan,
        'supported_countries': SUPPORTED_COUNTRIES,
        'supported_languages': SUPPORTED_LANGUAGES
    })


@app.route('/api/countries', methods=['GET'])
def get_countries():
    """Return list of supported cultural culinary regions."""
    from models.cultural_diets import SUPPORTED_COUNTRIES
    return jsonify({
        'success': True,
        'countries': SUPPORTED_COUNTRIES
    })


@app.route('/api/languages', methods=['GET'])
def get_languages():
    """Return list of supported languages for diet translation."""
    from models.cultural_diets import SUPPORTED_LANGUAGES
    return jsonify({
        'success': True,
        'languages': SUPPORTED_LANGUAGES
    })


@app.route('/api/disease/<condition>', methods=['GET'])
def get_disease_detail(condition):
    """Return clinical details for a specific disease code or name."""
    from models.skin_disease_model import DISEASE_CLASSES
    cond_lower = condition.lower()
    for d in DISEASE_CLASSES.values():
        if d['code'].lower() == cond_lower or d['name'].lower().replace(' ', '-') == cond_lower:
            return jsonify({
                'success': True,
                'disease': d
            })
    return jsonify({'error': f'Disease condition "{condition}" not found'}), 404


@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'model_loaded': MODEL is not None,
        'mode': 'production' if MODEL else 'demo',
        'benchmark_samples_count': len(BENCHMARK_SAMPLES)
    })


# ── Main ──────────────────────────────────────────────────
if __name__ == '__main__':
    load_model()
    print("\n[+] DermAI 360 server running at http://localhost:5000\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
