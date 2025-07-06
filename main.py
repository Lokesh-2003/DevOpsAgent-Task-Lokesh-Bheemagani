import requests
import os
import time
import logging
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Constants
PROMETHEUS_URL = "http://localhost:9090/api/v1/query"
SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = "#general"
CPU_THRESHOLD = float(os.getenv("CPU_THRESHOLD", 80))  # Default is 80%

# Logging config
logging.basicConfig(level=logging.INFO)

def get_cpu_usage():
    query = '100 - (avg by(instance)(irate(node_cpu_seconds_total{mode="idle"}[2m])) * 100)'
    try:
        response = requests.get(PROMETHEUS_URL, params={"query": query})
        data = response.json()
        usage = float(data["data"]["result"][0]["value"][1])
        logging.info(f"CPU usage: {usage}%")
        return usage
    except Exception as e:
        logging.error(f"Failed to fetch CPU usage: {e}")
        return None

def send_slack_alert(usage):
    if not SLACK_TOKEN:
        logging.error("SLACK_BOT_TOKEN not set.")
        return

    headers = {
        "Authorization": f"Bearer {SLACK_TOKEN}",
        "Content-type": "application/json; charset=utf-8"
    }
    payload = {
        "channel": SLACK_CHANNEL,
        "text": f":rotating_light: High CPU Alert! Current usage is {usage:.2f}%"
    }
    response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=payload)
    if response.status_code != 200 or not response.json().get("ok"):
        logging.error(f"Slack error: {response.text}")

def main():
    while True:
        cpu = get_cpu_usage()
        if cpu and cpu > CPU_THRESHOLD:
            send_slack_alert(cpu)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
