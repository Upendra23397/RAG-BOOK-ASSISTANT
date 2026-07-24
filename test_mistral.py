import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("MISTRAL_API_KEY")

print(key)