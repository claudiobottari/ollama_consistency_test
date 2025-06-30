from ollama import chat, ResponseError

def run_test(test_prompt: str,
             model_name="phi4-mini-reasoning:latest",
             options=None):
    responses = []
    for i in range(1000):
        try:
            resp = chat(
                model=model_name,
                messages=[{"role": "user", "content": test_prompt}],
                options=options or {"temperature": 0.0}
            )
            content = resp.message.content
            print(content)
            responses.append(content)
        except ResponseError as e:
            print(f"Error on iteration {i}: {e}")
            responses.append(None)
    return responses

def all_equal(lst):
    return bool(lst) and all(x == lst[0] for x in lst)

def main():
    test_prompt = """
You are a helpful assistant. Respond concisely.
User: What is the capital of France?
Assistant:
"""
    responses = run_test(
        test_prompt,
        options={"temperature": 0.0}
    )
    if all_equal(responses):
        print("All responses are identical.")
    else:
        print("Responses differ:", len(set(responses)), "unique outputs.")

if __name__ == "__main__":
    main()
