# src/core/policy_engine.py

def evaluate_risk(prompt, intent, outputs):
    score = 0

    risky_words = ["hack", "exploit", "bypass", "illegal"]

    for word in risky_words:
        if word in prompt.lower():
            score += 50

    return {
        "risk_score": score,
        "threshold": 70
    }
