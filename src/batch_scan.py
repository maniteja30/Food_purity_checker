import json
from pathlib import Path
from src.ocr import extract_text
from src.ner import isolate_ingredient_section, extract_ingredients
from src.matching import classify_ingredients

PHOTO_DIR = Path("data/raw/label_photos")
OUT_FILE = Path("data/processed/label_test_results.json")

def run():
    results = []
    for img in sorted(PHOTO_DIR.glob("*")):
        if img.suffix.lower() not in {".jpg", ".jpeg", ".png"}:
            continue
        text = " ".join(extract_text(img.read_bytes()))
        section = isolate_ingredient_section(text)
        ingredients = extract_ingredients(section)
        classified = classify_ingredients(ingredients)
        results.append({"image": img.name, "ocr_text": text, "ingredients": classified})
        print(f"done: {img.name}")
    OUT_FILE.write_text(json.dumps(results, indent=2))
    print(f"Processed {len(results)} images -> {OUT_FILE}")

if __name__ == "__main__":
    run()