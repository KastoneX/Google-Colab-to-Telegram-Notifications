import requests

# Replace 'YOUR_TELEGRAM_TOKEN' with your bot's API token
telegram_token = 'YOUR_TELEGRAM_TOKEN'
url = f'https://api.telegram.org/bot{telegram_token}/getUpdates'

response = requests.get(url)
data = response.json()

# Retrieve the chat ID from the latest updates
for result in data['result']:
    chat_id = result['message']['chat']['id']
    print(f'Chat ID: {chat_id}')
    break  # We only need one chat ID
