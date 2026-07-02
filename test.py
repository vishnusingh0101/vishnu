import ollama

response = ollama.chat(
    model="qwen3:4b",
    messages=[
        {
            "role": "user",
            "content": "Who are you?"
        }
    ]
)

print(response["message"]["content"])