import os
from dotenv import load_dotenv
load_dotenv()

BING_API_KEY = os.getenv('BING_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')