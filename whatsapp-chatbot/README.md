# WhatsApp Chatbot for Store

This project is a WhatsApp chatbot designed to assist with inventory management and billing for a store. The chatbot interacts with customers via WhatsApp, allowing them to inquire about products, check stock availability, and process payments.

## Project Structure

```
whatsapp-chatbot
├── src
│   ├── app.py          # Main entry point of the chatbot application
│   ├── inventory.py    # Manages the inventory system
│   ├── billing.py      # Handles billing operations
│   └── utils
│       └── __init__.py # Utility functions used across the application
├── requirements.txt     # Lists the project dependencies
├── config.py            # Configuration settings for the application
└── README.md            # Documentation for the project
```

## Features

- **Inventory Management**: 
  - Add, remove, and check stock of items.
  
- **Billing Operations**: 
  - Create invoices, process payments, and check invoice status.

- **WhatsApp Integration**: 
  - Communicate with customers through WhatsApp.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/whatsapp-chatbot.git
   cd whatsapp-chatbot
   ```

2. Install the required dependencies:
   ``` pip install -r requirements.txt
   ```
  

3. Configure the application:
   - Update the `config.py` file with your API keys, webhook URLs, and database connection strings.

4. Run the application:
   ```
   python src/app.py
   ```

## Usage Guidelines

- Send a message to the WhatsApp number associated with the chatbot to start interacting.
- Use commands to check inventory, inquire about products, and make payments.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.