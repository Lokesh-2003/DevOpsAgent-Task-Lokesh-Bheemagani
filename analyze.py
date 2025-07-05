import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_logs(logs):
    prompt = f"""
You are OpsBot, an AI DevOps assistant. Analyze the following logs and identify the most likely cause of high CPU usage. Suggest a potential remediation step if applicable.

Logs:
{logs}
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error during LLM analysis: {e}"
