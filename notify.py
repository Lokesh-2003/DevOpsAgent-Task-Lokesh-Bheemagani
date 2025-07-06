import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_TOKEN)

def send_alert(message):
    try:
        response = client.chat_postMessage(
            channel="#general",  # change if needed
            text=message
        )
        print("Slack alert sent.")
    except SlackApiError as e:
        print(f"Error sending Slack alert: {e}")
