from openai import OpenAI

# Локальный OpenAI-совместимый эндпоинт (Ollama или vLLM)
client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Что такое векторная база данных?"},
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
