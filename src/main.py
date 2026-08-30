from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Food Purity Checker API is running"}
