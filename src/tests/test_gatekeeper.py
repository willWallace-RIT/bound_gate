from src.core.gatekeeper import process_prompt

def test_basic_prompt():
    result = process_prompt("hello world")
    assert "decision" in result
