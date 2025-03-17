from flask import Flask, request
from flask_ngrok import run_with_ngrok
from inventory import Inventory
from billing import Billing
from utils import send_message, log_event

app = Flask(__name__)
run_with_ngrok(app)

inventory = Inventory()
billing = Billing()

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    log_event(data)

    if 'messages' in data:
        for message in data['messages']:
            handle_message(message)

    return '', 200

def handle_message(message):
    sender = message['from']
    text = message['text']['body']

    if text.startswith('add item'):
        item_details = text.split(' ', 2)[2]
        inventory.add_item(item_details, 1)  # Assuming quantity is 1 for simplicity
        send_message(sender, f'Item "{item_details}" added to inventory.')

    elif text.startswith('remove item'):
        item_details = text.split(' ', 2)[2]
        try:
            inventory.remove_item(item_details, 1)  # Assuming quantity is 1 for simplicity
            send_message(sender, f'Item "{item_details}" removed from inventory.')
        except ValueError as e:
            send_message(sender, str(e))

    elif text.startswith('check stock'):
        item_details = text.split(' ', 2)[2]
        stock = inventory.check_stock(item_details)
        send_message(sender, f'Stock for "{item_details}": {stock}')

    elif text.startswith('invoice'):
        invoice_details = text.split(' ', 1)[1]
        items = invoice_details.split(',')  # Assuming items are comma-separated
        total_amount = sum([inventory.check_stock(item) for item in items])  # Simplified total amount calculation
        invoice_id = len(billing.invoices) + 1
        invoice = billing.create_invoice(invoice_id, items, total_amount)
        send_message(sender, f'Invoice created: {invoice}')

    elif text.startswith('pay'):
        payment_details = text.split(' ', 1)[1]
        invoice_id, payment_amount = payment_details.split(',')
        status = billing.process_payment(int(invoice_id), float(payment_amount))
        send_message(sender, f'Payment status: {status}')

    elif text.startswith('invoice status'):
        invoice_id = text.split(' ', 2)[2]
        status = billing.get_invoice_status(int(invoice_id))
        send_message(sender, f'Invoice status: {status}')

if __name__ == '__main__':
    app.run()