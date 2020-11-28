from dotenv import load_dotenv
import os

# handle .env
load_dotenv()
TOKEN = os.getenv("TOKEN")
COOKIES = os.getenv("TOKEN")
JAM_CHECKOUT = os.getenv("JAM_CHECKOUT")
PRODUCT_URL = os.getenv("PRODUCT_URL")