import ollama

def chat(prompt: str):
    print(f"Received: {prompt}")

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("Response received")

    return response["message"]["content"]