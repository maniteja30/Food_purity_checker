from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Food Purity Checker API is running"}

@app.post("/scan")
async def scan_label(file: UploadFile = File(...)):
    contents = await file.read()
    return {"filename": file.filename, "size_bytes": len(contents)}