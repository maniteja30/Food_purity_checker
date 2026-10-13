WEIGHTS = {"natural": 1, "artificial": -1, "high-risk": -3}
def compute_purity_score(classified: list[dict]) -> dict:
    known = [item for item in classified if item["category"] in WEIGHTS]
    n = len(known)
    if(n == 0):
        return {"score": None, "category": "Unknown", "risk": 0, "coverage": 0.0}
    raw = sum(WEIGHTS[item["category"]] for item in known)
    worst = min(WEIGHTS.values())*n
    best = max(WEIGHTS.values())*n
    score = (raw - worst)/(best - worst) * 100

    risk = sum(-WEIGHTS[item["category"]] for item in known if WEIGHTS[item["category"]] < 0)

    if score >= 70:
        category = "Good Quality"
    elif score >= 40:
        category = "Moderately Processed"
    else:
        category = "Highly Processed"
    return {
        "score": round(score, 1),
        "category": category,
        "risk": risk,
        "coverage": round(n/len(classified), 2),
    }