from fastapi import FastAPI, UploadFile, File
from src.ocr import extract_text

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Food Purity Checker API is running"}

@app.post("/scan")
async def scan_label(file: UploadFile = File(...)) -> dict:
    contents = await file.read()
    extracted_text = extract_text(contents)
    return {"filename": file.filename, "extracted_text": extracted_text, "size_bytes": len(contents)}