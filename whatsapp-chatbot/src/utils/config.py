import os
from dotenv import load_dotenv

load_dotenv()

BILLING_FILE = "billing.json"
INVENTORY_FILE = "inventory.json"
DATABASE_URI = "sqlite:///your_database.db"
WEBHOOK_URL = "https://your_webhook_url_here"
API_KEY = os.getenv('TWILIO_API_KEY')