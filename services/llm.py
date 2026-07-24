import os
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI


load_dotenv()

_key = os.getenv("MISTRAL_API_KEY")
print("=" * 50)
print("DEBUG KEY:", repr(_key))
print("=" * 50)


def get_llm():
    llm = ChatMistralAI(
        model="mistral-small-2506",
        mistral_api_key=os.getenv("MISTRAL_API_KEY")
    )
    return llm