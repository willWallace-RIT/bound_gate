from src.core.gatekeeper import process_prompt

if __name__ == "__main__":
    prompt = input("Enter prompt: ")

    result = process_prompt(prompt)

    print("\n--- RESULT ---")
    print(result)
