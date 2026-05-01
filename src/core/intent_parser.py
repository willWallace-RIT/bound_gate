# src/core/intent_parser.py

def parse_intent(prompt: str):
    return {
        "raw": prompt,
        "keywords": prompt.lower().split(),
        "domain_guess": "unknown"
    }
