import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_questions(tech_stack):
    prompt = f"Generate 3 technical interview questions each for the following technologies:\n{', '.join(tech_stack)}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a technical recruiter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=500
    )

    return response.choices[0].message["content"]
