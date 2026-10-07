import json
from rapidfuzz import process, fuzz

with open("data/processed/ingredients_db.json") as f:
    INGREDIENT_DB = json.load(f)

def match_ingredient(ingredient: str, threshold: int = 80):
    match, score, _ = process.extractOne(
        ingredient, INGREDIENT_DB.keys(), scorer=fuzz.ratio
    )
    if score >= threshold:
        return match, INGREDIENT_DB[match]
    return ingredient, "unknown"

def classify_ingredients(ingredients: list[str]) -> list[dict]:
    results = []
    for ing in ingredients:
        matched_name, category = match_ingredient(ing)
        results.append({"ingredient": ing, "matched_as": matched_name, "category": category})
    return results