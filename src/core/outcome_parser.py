# src/core/outcome_simulator.py

def simulate_outputs(intent: dict):
    base = intent["raw"]

    return [
        f"Generated response based on: {base}",
        f"Expanded interpretation of: {base}",
        f"Edge-case output simulation for: {base}"
    ]
