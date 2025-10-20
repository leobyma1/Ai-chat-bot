import openai

# Set your API key (keep it secret!)
openai.api_key = "sk-nYVq2Xz7ltzTeruLQMv1Zo3dgxwSfczWzavEy98v2GdHUrHS"

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        return f"OpenAI API error: {e}"

user_input = "Hello GPT!"
reply = chat_with_gpt(user_input)
print(reply)
