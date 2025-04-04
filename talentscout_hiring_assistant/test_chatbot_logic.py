from chatbot_logic import handle_input

# This simulates a user talking to the chatbot
user_data = {}

# Greeting stage
msg, stage = handle_input("", "greeting", user_data)
print(f"🤖 Bot: {msg} (Next stage: {stage})")

# Name stage
msg, stage = handle_input("John Doe", stage, user_data)
print(f"🤖 Bot: {msg} (Next stage: {stage})")

# Email stage (valid)
msg, stage = handle_input("john@example.com", stage, user_data)
print(f"🤖 Bot: {msg} (Next stage: {stage})")

# Phone stage (invalid input first)
msg, stage = handle_input("12345", stage, user_data)
print(f"🤖 Bot: {msg} (Still at stage: {stage})")

# Try again with valid phone
msg, stage = handle_input("+91 9876543210", stage, user_data)
print(f"🤖 Bot: {msg} (Next stage: {stage})")

# End the conversation manually
msg, stage = handle_input("exit", stage, user_data)
print(f"🤖 Bot: {msg} (Stage: {stage})")
