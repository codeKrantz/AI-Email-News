from openai import OpenAI

client = OpenAI()

def generate_email_content(topic: str) -> str:
    prompt = f"Write an informative email about news on the following topic: {topic}"
    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes informative emails about news."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content