from groq import Groq
import os



def generate_response(prompt):
    client = Groq(api_key = os.getenv("GROQ_API_KEY"))

    completion = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages = [
            {
                "role": "user",
                "content": f'Resuma o texto a seguir: {prompt}'
            }
        ],
        temperature=0.6,
        max_completion_tokens=4096,
        top_p=0.95,
        reasoning_effort="default",
        stream=True,
        stop=None
    )

    # Variável para acumular toda a resposta
    full_response = ""

    for chunk in completion:
        delta = chunk.choices[0].delta.content
        if delta:
            full_response += delta  # Acumula o texto

    return full_response.split('</think>\n\n')[1]
