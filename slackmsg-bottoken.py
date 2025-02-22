import requests
import json

def slack_msg_token(message, bot_token, channel):

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bot_token}"
    }
    payload = {
        "channel": channel,
        "text": message
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200 and response.json()["ok"]:
        print(f"Message sent successfully to {channel}")
    else:
        print(f"Failed to send message to {channel}: {response.text}")


if __name__ == "__main__":

    bot_token = "xoxb-8216723433895-8356950436839-Dk3dn4YGxfEpk3vJTx3vkeNt"
    
    # List of channels to send messages to
    channels = ["U0875TR49HP", "#devopscicd", "C086LJLV8PQ"]
    message = "Hello from your Python script!"
    
    # Send the message to multiple channels
    for channel in channels:
        print(f"Sending message to {channel}...")
        slack_msg_token(message, bot_token, channel)