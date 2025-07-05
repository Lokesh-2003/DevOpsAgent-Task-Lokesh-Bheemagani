from slack_sdk import WebClient
import os
from dotenv import load_dotenv

load_dotenv()
client = WebClient(token=os.getenv("SLACK_TOKEN"))

def send_alert(message):
    try:
        client.chat_postMessage(channel=os.getenv("SLACK_CHANNEL"), text=message)
    except Exception as e:
        print(f"Error sending Slack alert: {e}")
