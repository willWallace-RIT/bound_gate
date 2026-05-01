from fastapi import FastAPI
from src.core.gatekeeper import process_prompt

app = FastAPI()

@app.post("/evaluate")
def evaluate(prompt: str):
    return process_prompt(prompt)
