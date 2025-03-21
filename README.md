# WhatsAppBot_Automation: Client Payment Reminder System

A Python automation tool that sends personalized payment reminders to clients via WhatsApp Web.

## Overview
This project automates the process of sending payment reminders to clients with different due dates. The system reads client data from an Excel spreadsheet, formats personalized messages containing the client's name and due date, and automatically sends these messages through WhatsApp Web.

## Features
- Reads client data from Excel files
- Generates personalized payment reminder messages
- Automates WhatsApp Web to send messages
- Records errors in a CSV file for follow-up
- Handles multiple clients with different payment dates

## Requirements
- Python 3.6+
- Required libraries:
  - openpyxl
  - Pillow
  - PyAutoGUI
  - webbrowser (standard library)
  - time (standard library)
  - urllib (standard library)

## Installation
1. Clone this repository
2. Install required packages: 
  - pip install openpyxl pillow pyautogui
3. Prepare your Excel file with client data:
   - The Excel file should be named `clientes.xlsx`
   - Column A: Client Name
   - Column B: Phone Number (with country code, only numbers)
   - Column C: Payment Due Date

4. Create a "send button" image:
   - Take a screenshot of the WhatsApp Web send button
   - Save it as `seta.png` in the project directory

## Usage
1. Run the script:
python app.py

2. The script will:
   - Open WhatsApp Web in your default browser
   - Wait for you to scan the QR code (first time only)
   - Process each client in the Excel file
   - Send personalized messages with payment links
   - Log any errors to errors.csv

## How It Works
1. The script loads client data from the Excel file
2. For each client, it:
   - Formats a personalized message with the payment due date
   - Opens WhatsApp Web with the client's phone number
   - Locates the send button using image recognition
   - Sends the message
   - Closes the tab before moving to the next client

## Error Handling
If a message cannot be sent, the script:
- Prints a notification to the console
- Records the client name and phone number in errors.csv for manual follow-up

## Important Notes
- This project uses web automation and not an official WhatsApp API
- The sample data in this repository is fictional and for demonstration purposes only
- Response times may vary based on your internet connection speed
- You must remain logged in to WhatsApp Web during execution

## Disclaimer
This tool is for personal or business use where you have proper consent to contact the individuals. Always comply with WhatsApp's terms of service and local regulations regarding automated messaging.

## License
6HTR66. This is a demonstration version project. All rights reserved.
