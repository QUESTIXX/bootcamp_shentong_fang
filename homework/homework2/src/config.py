import os
from dotenv import load_dotenv

def load_env():
    """Load environment variables from .env file."""
    load_dotenv()

def get_key():
    """Retrieve the API_KEY from environment variables."""
    load_dotenv()
    return os.getenv("API_KEY")