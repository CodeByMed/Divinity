'''
import requests
import json

DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

def send_message(content):
    data = {
        "content": content
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message: {response.status_code} - {response.text}")

def send_embed(title, description, color):
    embed = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color
            }
        ]
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=embed)
    if response.status_code == 204:
        print("Embed sent successfully.")
    else:
        print(f"Failed to send embed: {response.status_code} - {response.text}")

def set_webhook_url(url):
    global DISCORD_WEBHOOK_URL
    DISCORD_WEBHOOK_URL = url
    print("Webhook URL updated.")
'''