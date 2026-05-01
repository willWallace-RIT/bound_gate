# src/core/gatekeeper.py

from src.core.intent_parser import parse_intent
from src.core.outcome_simulator import simulate_outputs
from src.core.policy_engine import evaluate_risk
from src.core.escalation_router import route_decision

def process_prompt(prompt: str):
    intent = parse_intent(prompt)
    outputs = simulate_outputs(intent)
    risk = evaluate_risk(prompt, intent, outputs)
    decision = route_decision(risk)

    return {
        "prompt": prompt,
        "intent": intent,
        "risk": risk,
        "decision": decision
    }
