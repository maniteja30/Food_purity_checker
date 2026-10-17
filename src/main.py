from fastapi import FastAPI, UploadFile, File
from src.ocr import extract_text
from src.ner import extract_ingredients, isolate_ingredient_section
from src.matching import classify_ingredients
from src.scoring import compute_purity_score

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Food Purity Checker API is running"}

@app.post("/scan")
async def scan_label(file: UploadFile = File(...)) -> dict:
    contents = await file.read()
    extracted_text = extract_text(contents)
    full_text = " ".join(extracted_text)
    section = isolate_ingredient_section(full_text)
    ingredients = extract_ingredients(section)
    classified = classify_ingredients(ingredients)
    purity = compute_purity_score(classified)
    return {"filename": file.filename, "extracted_text": extracted_text, "ingredients:": classified, "purity:": purity}