def greeting_prompt():
    return "Hello! I’m TalentScout’s Hiring Assistant. I’ll help collect a few details and ask you some quick technical questions. Let’s get started!"

def info_prompt(field):
    prompts = {
        "name": "What is your full name?",
        "email": "Please share your email address:",
        "phone": "Can I get your phone number?",
        "experience": "How many years of experience do you have?",
        "position": "What position are you applying for?",
        "location": "Where are you currently located?",
        "tech_stack": "List the technologies you’re proficient in (e.g., Python, React, SQL):"
    }
    return prompts.get(field, "")

def generate_question_prompt(tech_stack):
    return f"Generate 3 technical interview questions for each of these technologies: {', '.join(tech_stack)}."

def fallback_prompt():
    return "I didn’t quite get that. Could you please rephrase?"
