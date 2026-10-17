import re

STOP_WORDS = ["nutrition", "allergen", "contains", "manufactured", "marketed", "best before", "storage", "net weight"]


def isolate_ingredient_section(text: str) -> str:
    lowered = text.lower()
    match = re.search(r"ingred[a-z]*\s*:?", lowered)
    if match is None:
        return ""
    section = lowered[match.end():]
    cut = len(section)
    for word in STOP_WORDS:
        idx = section.find(word)
        if idx != -1:
            cut = min(cut, idx)
    return section[:cut]


def extract_ingredients(text: str) -> list[str]:
    cleaned = text.lower()
    cleaned = re.sub(r"ingredients\s*:?", "", cleaned)
    cleaned = re.sub(r"\d+(\.\d+)?\s*%", "", cleaned)
    cleaned = re.sub(r"[()\[\];]", ",", cleaned)
    cleaned = re.sub(r"[^a-z0-9,\s\-]", "", cleaned)
    parts = cleaned.split(",")
    parts = [re.sub(r"\s+", " ", p).strip() for p in parts]
    return [p for p in parts if p]