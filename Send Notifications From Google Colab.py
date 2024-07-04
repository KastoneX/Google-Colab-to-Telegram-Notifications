import requests

# Replace 'YOUR_TELEGRAM_TOKEN' and 'YOUR_CHAT_ID' with your actual token and chat ID
telegram_token = 'YOUR_TELEGRAM_TOKEN'
chat_id = 'YOUR_CHAT_ID'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{telegram_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    return response

# Example: Send a notification
send_telegram_message('Process completed successfully!')
