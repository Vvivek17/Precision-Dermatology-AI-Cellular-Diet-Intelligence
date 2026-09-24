"""
Training Script for Skin Disease Detection Model
Dataset: HAM10000 (Human Against Machine with 10000 training images)
Download from: https://www.kaggle.com/datasets/kmader/skin-lesion-analysis-toward-melanoma-detection
"""

import os
import sys
import json
import argparse
import numpy as np
from pathlib import Path

# Force UTF-8 on Windows terminal to prevent charmap UnicodeEncodeErrors
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# ──────────────────────────────────────────────────────────
# CONFIGURATION
# ──────────────────────────────────────────────────────────
CONFIG = {
    "data_dir": "data/HAM10000",          # Path to dataset
    "model_save_path": "models/saved/skin_model.keras",
    "batch_size": 32,
    "image_size": (224, 224),
    "epochs": 30,
    "fine_tune_epochs": 10,
    "learning_rate": 1e-4,
    "fine_tune_lr": 1e-5,
    "val_split": 0.2,
    "test_split": 0.1,
    "seed": 42
}

CLASSES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
NUM_CLASSES = len(CLASSES)


def check_dependencies():
    missing = []
    for pkg in ['tensorflow', 'sklearn', 'PIL', 'pandas', 'matplotlib']:
        try:
            __import__(pkg if pkg != 'PIL' else 'PIL.Image')
        except ImportError:
            missing.append(pkg)
    return missing


def load_and_split_data(data_dir=None):
    """Load HAM10000 metadata and split into train/val/test."""
    import pandas as pd
    from sklearn.model_selection import train_test_split

    data_dir = data_dir or CONFIG["data_dir"]
    meta_path = os.path.join(data_dir, "HAM10000_metadata.csv")
    if not os.path.exists(meta_path):
        alt_meta = os.path.join(data_dir, "metadata.csv")
        if os.path.exists(alt_meta):
            meta_path = alt_meta
        else:
            print(f"❌ Dataset metadata not found at {meta_path}")
            print(f"   Ensure HAM10000_metadata.csv is placed inside {data_dir}/")
            print("📥 Download from: https://www.kaggle.com/datasets/kmader/skin-lesion-analysis-toward-melanoma-detection")
            print("\n💡 To test single-image AI diagnosis or view targeted diet plans:")
            print("   Run CLI:  python predict_cli.py data/HAM10000/images/ISIC_0000001.jpg")
            print("   Run Web:  python app.py  (then open http://localhost:5000 in your browser)")
            sys.exit(1)

    df = pd.read_csv(meta_path)

    # Ensure image_id has .jpg extension for image generators
    if 'image_id' in df.columns and len(df) > 0:
        if not str(df['image_id'].iloc[0]).lower().endswith(('.jpg', '.jpeg', '.png')):
            df['image_id'] = df['image_id'].astype(str) + '.jpg'

    # Filter to only images that exist in images/ directory
    img_dir = os.path.join(data_dir, "images")
    if os.path.exists(img_dir):
        available_files = set(os.listdir(img_dir))
        initial_count = len(df)
        df = df[df['image_id'].isin(available_files)].reset_index(drop=True)
        if len(df) < initial_count:
            print(f"ℹ️  Filtered dataset to {len(df)} images currently present in {img_dir} (from {initial_count} total rows in CSV)")

    if len(df) == 0:
        print(f"❌ No matching images found in {img_dir} for entries in {meta_path}")
        sys.exit(1)

    print(f"✅ Loaded {len(df)} samples")
    print(f"   Class distribution:\n{df['dx'].value_counts()}")

    # Split
    train_df, test_df = train_test_split(df, test_size=CONFIG["test_split"], stratify=df['dx'], random_state=CONFIG["seed"])
    train_df, val_df = train_test_split(train_df, test_size=CONFIG["val_split"], stratify=train_df['dx'], random_state=CONFIG["seed"])

    print(f"\n   Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")
    return train_df, val_df, test_df


def create_data_generators(train_df, val_df, test_df, img_dir):
    """Create augmented data generators for training."""
    import tensorflow as tf
    try:
        ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator
    except AttributeError:
        from keras.src.legacy.preprocessing.image import ImageDataGenerator

    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range=0.15,
        horizontal_flip=True,
        vertical_flip=True,
        brightness_range=[0.8, 1.2],
        fill_mode='nearest'
    )

    val_gen = ImageDataGenerator(rescale=1./255)

    train_flow = train_gen.flow_from_dataframe(
        train_df, directory=img_dir, x_col='image_id',
        y_col='dx', target_size=CONFIG["image_size"],
        batch_size=CONFIG["batch_size"], class_mode='categorical',
        classes=CLASSES
    )
    val_flow = val_gen.flow_from_dataframe(
        val_df, directory=img_dir, x_col='image_id',
        y_col='dx', target_size=CONFIG["image_size"],
        batch_size=CONFIG["batch_size"], class_mode='categorical',
        classes=CLASSES, shuffle=False
    )
    test_flow = val_gen.flow_from_dataframe(
        test_df, directory=img_dir, x_col='image_id',
        y_col='dx', target_size=CONFIG["image_size"],
        batch_size=CONFIG["batch_size"], class_mode='categorical',
        classes=CLASSES, shuffle=False
    )
    return train_flow, val_flow, test_flow


def compute_class_weights(train_df):
    """Handle class imbalance with weighted loss."""
    from sklearn.utils.class_weight import compute_class_weight
    classes = np.array(range(NUM_CLASSES))
    y = train_df['dx'].map({c: i for i, c in enumerate(CLASSES)}).values
    weights = compute_class_weight('balanced', classes=classes, y=y)
    return dict(enumerate(weights))


def build_and_train(train_flow, val_flow, class_weights):
    """Build model and run two-phase training."""
    import keras
    from keras.applications import EfficientNetB3
    from keras import layers, Model
    from keras.callbacks import (
        EarlyStopping, ReduceLROnPlateau, ModelCheckpoint, TensorBoard
    )

    # ── Phase 1: Train head only ──────────────────────────
    print("\n🔥 Phase 1: Training classification head...")
    base = EfficientNetB3(include_top=False, weights='imagenet',
                          input_shape=(*CONFIG["image_size"], 3))
    base.trainable = False

    x = base.output
    x = layers.GlobalAveragePooling2D()(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(512, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    x = layers.Dense(256, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    outputs = layers.Dense(NUM_CLASSES, activation='softmax')(x)

    model = Model(inputs=base.input, outputs=outputs)
    model.compile(
        optimizer=keras.optimizers.Adam(CONFIG["learning_rate"]),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc')]
    )

    os.makedirs(os.path.dirname(CONFIG["model_save_path"]), exist_ok=True)

    callbacks_p1 = [
        EarlyStopping(patience=5, restore_best_weights=True, monitor='val_auc', mode='max'),
        ReduceLROnPlateau(factor=0.5, patience=3, monitor='val_loss'),
        ModelCheckpoint(CONFIG["model_save_path"], save_best_only=True, monitor='val_auc', mode='max'),
        TensorBoard(log_dir='logs/phase1')
    ]

    history1 = model.fit(
        train_flow, validation_data=val_flow,
        epochs=CONFIG["epochs"],
        class_weight=class_weights,
        callbacks=callbacks_p1
    )

    # ── Phase 2: Fine-tune top layers ─────────────────────
    print("\n🔥 Phase 2: Fine-tuning top layers...")
    base.trainable = True
    # Freeze all layers except the last 30
    for layer in base.layers[:-30]:
        layer.trainable = False

    model.compile(
        optimizer=keras.optimizers.Adam(CONFIG["fine_tune_lr"]),
        loss='categorical_crossentropy',
        metrics=['accuracy', keras.metrics.AUC(name='auc')]
    )

    callbacks_p2 = [
        EarlyStopping(patience=5, restore_best_weights=True, monitor='val_auc', mode='max'),
        ReduceLROnPlateau(factor=0.5, patience=3, monitor='val_loss'),
        ModelCheckpoint(CONFIG["model_save_path"], save_best_only=True, monitor='val_auc', mode='max'),
        TensorBoard(log_dir='logs/phase2')
    ]

    history2 = model.fit(
        train_flow, validation_data=val_flow,
        epochs=CONFIG["fine_tune_epochs"],
        class_weight=class_weights,
        callbacks=callbacks_p2
    )

    return model, history1, history2


def evaluate_model(model, test_flow):
    """Evaluate and print classification report."""
    from sklearn.metrics import classification_report, confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns

    print("\n📊 Evaluating on test set...")
    test_flow.reset()
    preds = model.predict(test_flow, verbose=1)
    y_pred = np.argmax(preds, axis=1)
    y_true = test_flow.classes

    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=CLASSES))

    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=CLASSES, yticklabels=CLASSES, cmap='Blues')
    plt.title('Confusion Matrix - Skin Disease Detector')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig('models/saved/confusion_matrix.png', dpi=150)
    print("✅ Confusion matrix saved to models/saved/confusion_matrix.png")


def save_training_metadata():
    """Save class mappings and config for inference."""
    from models.skin_disease_model import DISEASE_CLASSES
    meta = {
        "classes": CLASSES,
        "disease_info": DISEASE_CLASSES,
        "config": CONFIG,
        "input_shape": [*CONFIG["image_size"], 3]
    }
    with open('models/saved/metadata.json', 'w') as f:
        json.dump(meta, f, indent=2)
    print("✅ Metadata saved to models/saved/metadata.json")


# ──────────────────────────────────────────────────────────
# MAIN
# ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Check if user passed an image file as input to train.py
    image_exts = ('.jpg', '.jpeg', '.png', '.webp', '.bmp')
    image_args = [arg for arg in sys.argv[1:] if arg.lower().endswith(image_exts)]
    if image_args:
        img_target = image_args[0]
        print("=" * 64)
        print(f"  💡 Notice: '{img_target}' is a lesion image.")
        print("     `train.py` is for training neural network weights on HAM10000.")
        print(f"     Redirecting to diagnostic inference: python predict_cli.py {img_target}")
        print("=" * 64)
        import subprocess
        result = subprocess.run([sys.executable, "predict_cli.py", img_target])
        sys.exit(result.returncode)

    # If executed without CLI flags, provide an interactive, welcoming menu
    if len(sys.argv) == 1:
        print("=" * 66)
        print("  🔬 DermAI 360 — Precision Dermatology & Cellular Nutrition AI")
        print("=" * 66)
        print("  Please select what you would like to do:\n")
        print("  [1] Diagnose skin lesion image & synthesize diet plan (Interactive)")
        print("  [2] Launch Web Dashboard (http://localhost:5000)")
        print("  [3] Run Model Training Pipeline on HAM10000 dataset")
        print("  [4] Quick Dataset Validation / Dry-Run (--dry-run)")
        print("  [5] Exit\n")
        try:
            choice = input("Enter choice [1-5] (default: 1): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)

        if choice in ('', '1'):
            import subprocess
            subprocess.run([sys.executable, "predict_cli.py"])
            sys.exit(0)
        elif choice == '2':
            import subprocess
            print("\n[+] Starting Web Dashboard on http://localhost:5000 ...")
            subprocess.run([sys.executable, "app.py"])
            sys.exit(0)
        elif choice == '4':
            sys.argv.append('--dry-run')
        elif choice == '5':
            print("Exiting.")
            sys.exit(0)
        elif choice != '3':
            print("Invalid choice, launching interactive diagnostic tool.")
            import subprocess
            subprocess.run([sys.executable, "predict_cli.py"])
            sys.exit(0)

    parser = argparse.ArgumentParser(description="Train Skin Disease Classification Model on HAM10000 Dataset")
    parser.add_argument("--data-dir", default=CONFIG["data_dir"], help="Path to directory containing HAM10000_metadata.csv and images/")
    parser.add_argument("--epochs", type=int, default=CONFIG["epochs"], help="Phase 1 epochs (default: 30)")
    parser.add_argument("--fine-tune-epochs", type=int, default=CONFIG["fine_tune_epochs"], help="Phase 2 epochs (default: 10)")
    parser.add_argument("--batch-size", type=int, default=CONFIG["batch_size"], help="Batch size (default: 32)")
    parser.add_argument("--dry-run", action="store_true", help="Validate data loading and generator pipeline without running full training")
    args = parser.parse_args()

    CONFIG["data_dir"] = args.data_dir
    CONFIG["epochs"] = args.epochs
    CONFIG["fine_tune_epochs"] = args.fine_tune_epochs
    CONFIG["batch_size"] = args.batch_size

    print("=" * 60)
    print("  🔬 Skin Disease Detection - Training Pipeline")
    print(f"  📂 Dataset Directory: {CONFIG['data_dir']}")
    print("=" * 60)

    missing = check_dependencies()
    if missing:
        print(f"❌ Missing dependencies: {missing}")
        print("   Run: pip install -r requirements.txt")
        sys.exit(1)

    img_dir = os.path.join(CONFIG["data_dir"], "images")
    train_df, val_df, test_df = load_and_split_data(CONFIG["data_dir"])
    train_flow, val_flow, test_flow = create_data_generators(train_df, val_df, test_df, img_dir)
    class_weights = compute_class_weights(train_df)

    print(f"\n⚖️  Class weights: {class_weights}")

    if args.dry_run:
        print("\n✨ Dry run completed successfully! Data pipeline and generators verified.")
        sys.exit(0)

    model, h1, h2 = build_and_train(train_flow, val_flow, class_weights)
    evaluate_model(model, test_flow)
    save_training_metadata()

    print("\n✅ Training complete!")
    print(f"   Model saved to: {CONFIG['model_save_path']}")
    print("   Run: python app.py  →  to start the web server")
