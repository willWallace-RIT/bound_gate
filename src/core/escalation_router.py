# src/core/escalation_router.py

def route_decision(risk):
    if risk["risk_score"] >= risk["threshold"]:
        return "ESCALATE_REVIEW"

    if risk["risk_score"] >= 40:
        return "CONSTRAIN_OUTPUT"

    return "ALLOW"
