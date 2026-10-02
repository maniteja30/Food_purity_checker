import re

def extract_ingredients(text: str) -> list[str]:
    cleaned = text.lower()
    cleaned = re.sub(r"ingredients:?", "", cleaned)
    cleaned = re.sub(r"[^a-z0-9, \s%\-]", "", cleaned)
    parts = cleaned.split(",")
    ingredients = [p.strip() for p in parts if p.strip()]
    return ingredients