"""
DermAI — CLI Clinical & Nutritional Inference Tool
Predicts skin disease, outputs disease profile, and provides targeted cellular diet plan.
Usage:
    python predict_cli.py path/to/image.jpg
    python predict_cli.py path/to/image.jpg --model models/saved/skin_model.keras
"""

import sys
import os

# Fix Windows console UTF-8 output encoding if possible
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


def main():
    image_path = None
    model_path = None

    if '--model' in sys.argv:
        idx = sys.argv.index('--model')
        if idx + 1 < len(sys.argv):
            model_path = sys.argv[idx + 1]

    # Find positional arg (image path)
    positional = [a for i, a in enumerate(sys.argv[1:], 1) if a != '--model' and sys.argv[i-1] != '--model']
    if positional:
        image_path = positional[0]

    if not image_path:
        print("\n" + "=" * 68)
        print("  🔬 DERMAI 360 - CLINICAL & NUTRITIONAL INFERENCE CLI")
        print("=" * 68)
        print("  Available demo samples: ISIC_0000000.jpg ... ISIC_0000006.jpg")
        try:
            prompt_val = input("\nEnter skin lesion image path (or press Enter for sample 'ISIC_0000001.jpg'): ").strip(' "\'')
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)
        image_path = prompt_val if prompt_val else "data/HAM10000/images/ISIC_0000001.jpg"

    # Search for image in local path, samples dir, HAM10000 dir
    if not os.path.exists(image_path):
        candidates = [
            os.path.join("data", "HAM10000", "images", os.path.basename(image_path)),
            os.path.join("data", "samples", os.path.basename(image_path)),
            os.path.join("uploads", os.path.basename(image_path))
        ]
        found = False
        for c in candidates:
            if os.path.exists(c):
                image_path = c
                found = True
                break
        if not found:
            print(f"[!] File not found: {image_path}")
            print("    Please provide a valid image path or sample name (e.g. data/HAM10000/images/ISIC_0000001.jpg)")
            sys.exit(1)

    model = None
    if model_path:
        if not os.path.exists(model_path):
            print(f"[!] Model not found at {model_path}, using intelligent simulation mode.")
        else:
            try:
                import tensorflow as tf
                print(f"[*] Loading model from {model_path}...")
                model = tf.keras.models.load_model(model_path)
                print("[+] Model loaded.")
            except Exception as e:
                print(f"[!] Could not load model: {e}")
    else:
        print("[i] Running in DEMO/simulation mode.")
        print("    Pass --model path/to/skin_model.keras for trained weights.\n")

    from models.skin_disease_model import predict_disease
    result = predict_disease(image_path, model)

    sep = "=" * 68
    subsep = "-" * 68

    print(f"\n{sep}")
    print("  [+] DERMAI 360 - CLINICAL & NUTRITIONAL INTELLIGENCE REPORT")
    print(sep)
    print(f"  Image File       : {os.path.basename(image_path)}")
    print(f"  Primary Disease  : {result['disease']} ({result.get('scientific_name', '')})")
    print(f"  Confidence Score : {result['confidence']}%")
    print(f"  Severity Level   : {result['severity']}")
    print(f"  Clinical Urgency : {result.get('urgency', result['severity'])}")
    print(f"  Image Specs      : {result['image_metrics'].get('dimensions', 'N/A')} (Luminance: {result['image_metrics'].get('mean_luminance', 'N/A')})")
    print(subsep)

    print("\n  [+] CLINICAL OVERVIEW:")
    print(f"  {result['description']}")

    clin = result.get('clinical_profile', {})
    if clin:
        print(f"\n  [+] PATHOPHYSIOLOGY:")
        print(f"  {clin.get('pathophysiology', 'N/A')}")
        print("\n  [+] DERMOSCOPY HALLMARKS:")
        for h in clin.get('dermoscopy_hallmarks', []):
            print(f"   * {h}")
        print("\n  [+] GOLD-STANDARD TREATMENTS:")
        for t in clin.get('standard_treatments', []):
            print(f"   * {t}")

    diet = result.get('diet_plan', {})
    if diet:
        # Parse Cultural & Language Options
        country_arg = "india"
        pref_arg = "non_veg"
        lang_arg = "en"
        if "--country" in sys.argv:
            c_idx = sys.argv.index("--country")
            if c_idx + 1 < len(sys.argv):
                country_arg = sys.argv[c_idx + 1].lower()
        if "--veg" in sys.argv or "--vegetarian" in sys.argv:
            pref_arg = "vegetarian"
        if "--nonveg" in sys.argv or "--non-veg" in sys.argv or "--omnivore" in sys.argv:
            pref_arg = "non_veg"
        if "--lang" in sys.argv:
            l_idx = sys.argv.index("--lang")
            if l_idx + 1 < len(sys.argv):
                lang_arg = sys.argv[l_idx + 1].lower()

        from models.cultural_diets import get_cultural_diet_plan
        cultural_dict = get_cultural_diet_plan(result.get("code", "mel"), country=country_arg, preference=pref_arg, lang=lang_arg)
        trans = cultural_dict.get("translations", {})
        track_name = trans.get("non_veg" if pref_arg == "non_veg" else "vegetarian", pref_arg.upper())

        phil = cultural_dict.get('diet_philosophy') or diet.get('philosophy', 'Skin Health')
        rat = cultural_dict.get('diet_rationale') or diet.get('rationale', 'Cellular repair')

        print(f"\n{subsep}")
        print(f"  [+] TARGETED CELLULAR DIET PLAN & NUTRITIONAL PROTOCOL (Lang: {lang_arg.upper()})")
        print(subsep)
        print(f"  Philosophy : {phil}")
        print(f"  Rationale  : {rat}")

        print("\n  [+] THERAPEUTIC SUPERFOODS:")
        for sf in diet.get('superfoods', []):
            print(f"   * {sf.get('icon', '+')} {sf['name']} ({sf['nutrient']})")
            print(f"     Action : {sf['cellular_action']}")
            print(f"     Sources: {sf['sources']}")

        print("\n  [+] FOODS & TRIGGERS TO AVOID:")
        for fa in diet.get('foods_to_avoid', []):
            print(f"   x {fa['category']}: {fa['reason']}")

        if cultural_dict:
            print(f"\n{subsep}")
            print(f"  [+] CULTURAL DIET PROTOCOL: {cultural_dict.get('flag', '')} {cultural_dict.get('country_name', 'Global')} [{track_name}] (Lang: {lang_arg.upper()})")
            print(f"      Focus: {cultural_dict.get('culinary_focus', '')}")
            print(subsep)

            c_meals = cultural_dict.get("meals", {})
            b_label = trans.get("breakfast", "BREAKFAST")
            l_label = trans.get("lunch", "LUNCH")
            d_label = trans.get("dinner", "DINNER")
            h_label = trans.get("hydration", "HYDRATION RITUAL")

            ing_label = trans.get("regional_ingredients", "Ingredients")

            if "breakfast" in c_meals:
                b = c_meals["breakfast"]
                print(f"   * 🌅 {b_label} ({b.get('timing', '8:00 AM')}):")
                print(f"     Dish   : {b.get('title', '')}")
                print(f"     {ing_label}: {b.get('ingredients', '')}")
                print(f"     Target : {b.get('action', '')}")
            if "lunch" in c_meals:
                l = c_meals["lunch"]
                print(f"   * 🥗 {l_label} ({l.get('timing', '1:00 PM')}):")
                print(f"     Dish   : {l.get('title', '')}")
                print(f"     {ing_label}: {l.get('ingredients', '')}")
                print(f"     Target : {l.get('action', '')}")
            if "dinner" in c_meals:
                d = c_meals["dinner"]
                print(f"   * 🍲 {d_label} ({d.get('timing', '7:00 PM')}):")
                print(f"     Dish   : {d.get('title', '')}")
                print(f"     {ing_label}: {d.get('ingredients', '')}")
                print(f"     Target : {d.get('action', '')}")
            if "hydration" in c_meals:
                h = c_meals["hydration"]
                print(f"   * 💧 {h_label} ({h.get('timing', '')}):")
                print(f"     Drink  : {h.get('title', '')}")
                print(f"     {ing_label}: {h.get('ingredients', '')}")
                print(f"     Action : {h.get('action', '')}")

            subs = cultural_dict.get("local_substitutions", [])
            if subs:
                print("\n  [+] REGIONAL INGREDIENT SUBSTITUTIONS:")
                for sub in subs:
                    print(f"   * {sub}")

    print(f"\n{subsep}")
    print("  [+] TOP DIFFERENTIAL DIAGNOSES:")
    for i, pred in enumerate(result['top_predictions'], 1):
        bar_len = int(pred['probability'] / 4)
        bar = '#' * bar_len
        print(f"  {i}. {pred['disease']:<26} {pred['probability']:5.1f}% [{bar:<25}]")

    print(f"\n  [!] {result['disclaimer']}\n")
    print(sep + "\n")


if __name__ == "__main__":
    main()
