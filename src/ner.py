import re

def extract_ingredients(text: str) -> list[str]:
    cleaned = text.lower()
    cleaned = re.sub(r"ingredients\s*:?", "", cleaned)
    cleaned = re.sub(r"\d+(\.\d+)?\s*%", "", cleaned)
    cleaned = re.sub(r"[()\[\];]", ",", cleaned)
    cleaned = re.sub(r"[^a-z0-9,\s\-]", "", cleaned)
    parts = cleaned.split(",")
    parts = [re.sub(r"\s+", " ", p).strip() for p in parts]
    return [p for p in parts if p]