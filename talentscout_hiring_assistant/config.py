import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EXIT_KEYWORDS = ["exit", "quit", "bye", "end", "stop"]
DEFAULT_TECH_STACK = ["Python", "Django", "React", "SQL"]
print("✅ API key loaded:", OPENAI_API_KEY[:5] + "..." if OPENAI_API_KEY else "❌ Not found")
