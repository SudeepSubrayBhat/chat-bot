from twilio.rest import Client
from config import API_KEY

def send_message(recipient, message):
    client = Client(API_KEY, API_KEY)
    client.messages.create(
        body=message,
        from_='whatsapp:+14155238886',  # Twilio sandbox number
        to=f'whatsapp:{recipient}'
    )

def log_event(event):
    # Function to log events for debugging and monitoring
    pass