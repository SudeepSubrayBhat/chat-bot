class Billing:
    def __init__(self):
        self.invoices = {}

    def create_invoice(self, invoice_id, items, total_amount):
        invoice = {
            'id': invoice_id,
            'items': items,
            'total_amount': total_amount,
            'status': 'unpaid'
        }
        self.invoices[invoice_id] = invoice
        return invoice

    def process_payment(self, invoice_id, payment_amount):
        if invoice_id in self.invoices:
            invoice = self.invoices[invoice_id]
            if payment_amount >= invoice['total_amount']:
                invoice['status'] = 'paid'
                return 'Payment successful'
            else:
                return 'Insufficient payment amount'
        else:
            return 'Invoice not found'

    def get_invoice_status(self, invoice_id):
        if invoice_id in self.invoices:
            return self.invoices[invoice_id]['status']
        else:
            return 'Invoice not found'