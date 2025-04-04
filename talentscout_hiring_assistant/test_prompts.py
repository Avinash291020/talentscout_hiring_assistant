from prompts import greeting_prompt, info_prompt, fallback_prompt

print("👋 Greeting Message:")
print(greeting_prompt())

print("\n🙋‍♂️ Name Prompt:")
print(info_prompt("name"))

print("\n💼 Tech Stack Prompt:")
print(info_prompt("tech_stack"))

print("\n❓ Unknown Field Prompt:")
print(info_prompt("unknown"))

print("\n😕 Fallback Response:")
print(fallback_prompt())
