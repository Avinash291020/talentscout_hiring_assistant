from tech_questions import generate_questions

# Let's test with a simple tech stack
test_stack = ["Python", "SQL"]

print("⏳ Generating questions for:", test_stack)
questions = generate_questions(test_stack)

print("\n✅ Questions received:")
print(questions)
