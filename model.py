import openai

def query_llm(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant helping to navigate and extract information from web pages."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content