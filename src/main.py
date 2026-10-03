from fastapi import FastAPI, UploadFile, File
from src.ocr import extract_text
from src.ner import extract_ingredients
from src.matching import classify_ingredients

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Food Purity Checker API is running"}

@app.post("/scan")
async def scan_label(file: UploadFile = File(...)) -> dict:
    contents = await file.read()
    extracted_text = extract_text(contents)
    full_text = " ".join(extracted_text)
    ingredients = extract_ingredients(full_text)
    classified = classify_ingredients(ingredients)
    return {"filename": file.filename, "extracted_text": extracted_text, "ingredients:": classified}