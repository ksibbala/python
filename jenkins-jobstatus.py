import requests
import json

jenkins_url = 'http://localhost:8080/job/jenkinsjobstatus/lastBuild/api/json'  
slack_webhook_url = "https://hooks.slack.com/services/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"

# Get Jenkins build status from API
response = requests.get(jenkins_url)
if response.status_code != 200:
    print(f"Failed to get Jenkins build status: {response.status_code}")
    exit(1)

build_status = response.json().get('result') 

message = f"Jenkins Build Status: *{build_status}*"
slack_payload = {
    "text": message,
    "username": "JenkinsBot", 
}

# Send Slack notification
slack_response = requests.post(slack_webhook_url, json=slack_payload)
if slack_response.status_code == 200:
    print("✅ Slack notification sent successfully")
else:
    print(f"❌ Failed to send Slack notification: {slack_response.text}")
