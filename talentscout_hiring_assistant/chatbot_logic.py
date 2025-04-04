from prompts import greeting_prompt, info_prompt, generate_question_prompt, fallback_prompt
from tech_questions import generate_questions
from utils import is_valid_email, is_valid_phone, should_end_conversation
from data_handler import save_candidate_data, log_interaction

fields = ["name", "email", "phone", "experience", "position", "location", "tech_stack"]

def handle_input(user_input, stage, user_data):
    log_interaction(f"User: {user_input}")
    
    if should_end_conversation(user_input):
        return "Thank you for your time! We'll get back to you shortly.", "end"

    if stage == "greeting":
        return info_prompt("name"), "name"

    if stage in fields:
        if stage == "email" and not is_valid_email(user_input):
            return "That doesn't look like a valid email. Please try again.", stage
        if stage == "phone" and not is_valid_phone(user_input):
            return "Please enter a valid phone number.", stage

        user_data[stage] = user_input

        next_stage_index = fields.index(stage) + 1
        if next_stage_index < len(fields):
            next_stage = fields[next_stage_index]
            return info_prompt(next_stage), next_stage
        else:
            questions = generate_questions(user_data.get("tech_stack", "").split(","))
            user_data["tech_questions"] = questions
            save_candidate_data(user_data)
            return f"Thanks for the info! Here are your questions:\n\n{questions}", "end"

    return fallback_prompt(), stage
