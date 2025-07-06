import os
import requests

def send_slack_alert(message):
    slack_token = os.getenv('SLACK_BOT_TOKEN')
    slack_channel = "#general"  # or use os.getenv("SLACK_CHANNEL")

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {slack_token}",
        "Content-type": "application/json; charset=utf-8"
    }

    payload = {
        "channel": slack_channel,
        "text": message
    }

    response = requests.post(url, json=payload, headers=headers)

    if not response.ok or not response.json().get("ok"):
        print("Error sending Slack alert:", response.json())
    else:
        print("✅ Slack alert sent successfully!")
