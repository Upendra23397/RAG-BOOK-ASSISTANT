import os
from dotenv import load_dotenv


load_dotenv()


MISTRAL_API_KEY = os.getenv(
    "MISTRAL_API_KEY"
)

OPENAI_API_KEY = os.getenv(
    "GOOGLE_API_KEY"
)


CHROMA_PATH = "data/chroma_db"
UPLOAD_PATH = "data/uploads"