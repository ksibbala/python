import requests
import json

def send_slack_message_via_webhook(message, webhook_url):
    payload = {
        "text": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print("Message sent successfully via webhook!")
    else:
        print(f"Failed to send message: {response.text}")

if __name__ == "__main__":
  
    webhook_url = "https://hooks.slack.com/services/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"
    message = "Sending slack notiofication via python script"
    send_slack_message_via_webhook(message, webhook_url)