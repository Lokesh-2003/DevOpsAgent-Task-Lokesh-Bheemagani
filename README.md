# 🤖 DevOps AI Agent

A smart infrastructure monitoring agent that uses:
- 📊 Prometheus to fetch real-time metrics
- ⚠️ Auto-detection of CPU spikes
- 🔔 Slack integration for alerts
- ☁️ Deployed on AWS EC2 (Free Tier)

## 🔧 Setup

1. Clone this repo:
```bash
git clone https://github.com/Lokesh-2003/DevOpsAgent-Task-Lokesh-Bheemagani.git
pip install -r requirements.txt
SLACK_BOT_TOKEN=your-bot-token
CPU_THRESHOLD=80
python3 main.py
