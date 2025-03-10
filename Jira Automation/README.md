# Automate JIRA Creation on a GitHub Event using Python

## Introduction
This guide explains how to automate JIRA ticket creation using Python whenever a GitHub event occurs. The integration leverages the JIRA REST API and the `requests` library to interact with JIRA.

## Prerequisites
Before proceeding, ensure you have the following:
- A JIRA account with API access.
- A GitHub repository where events will be triggered.
- Python installed on your system.
- The `requests` library installed (`pip install requests`).

## Setup Instructions

### 1. Install Dependencies
Ensure you have the `requests` library installed:
```bash
pip install requests
```

### 2. Define Authentication and API URL
Use Basic Authentication with your JIRA email and API token:

```python
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yourdomain.atlassian.net/rest/api/3/project"

auth = HTTPBasicAuth("your-email@example.com", "your-api-token")

headers = {
  "Accept": "application/json"
}
```

### 3. Fetch JIRA Projects
To retrieve all projects from JIRA:

```python
response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

for item in output:
    print(item["name"])
```

### 4. Automate JIRA Issue Creation on GitHub Event
To automate issue creation when a GitHub event occurs, set up a webhook in GitHub and modify the script to listen for events.

#### Example JIRA Issue Creation
```python
issue_url = "https://yourdomain.atlassian.net/rest/api/3/issue"

data = {
    "fields": {
        "project": {"key": "PROJ"},
        "summary": "New Issue from GitHub Event",
        "description": "This issue was created automatically from a GitHub event.",
        "issuetype": {"name": "Task"}
    }
}

response = requests.post(
    issue_url,
    headers={"Content-Type": "application/json", "Accept": "application/json"},
    auth=auth,
    data=json.dumps(data)
)

print(response.status_code, response.text)
```

### 5. Setting Up a GitHub Webhook
1. Navigate to your GitHub repository.
2. Go to **Settings** > **Webhooks**.
3. Click **Add webhook**.
4. Enter your server URL that listens for GitHub events.
5. Choose the event types you want to trigger JIRA issue creation (e.g., `issues`).
6. Save the webhook.

**[Insert Screenshot: Creating GitHub Webhook]**

### 6. Running the `github-jira.py` Script on an EC2 Instance
1. Upload the script to your EC2 instance.
2. Run the script:
```bash
python github-jira.py
```
3. Copy the **Public IPv4 DNS** of your EC2 instance and use it as the webhook URL in GitHub.

**[Insert Screenshot: Copying EC2 Public IPv4 DNS]**

### 7. Creating a GitHub Issue and Commenting `/Jira`
- Create an issue in GitHub.
- Add a comment with `/Jira` to trigger ticket creation.
- Verify the issue in JIRA.

**[Insert Screenshot: Creating Issue and Commenting /Jira]**
**[Insert Screenshot: Verifying Issue in JIRA]**

## HTTP Methods Explained

| Method  | Description |
|---------|-------------|
| **GET** | Retrieves data from the server (e.g., fetch JIRA issues). |
| **POST** | Sends new data to the server (e.g., create a JIRA issue). |
| **PUT** | Updates existing data on the server (e.g., modify a JIRA issue). |
| **DELETE** | Removes data from the server (e.g., delete a JIRA issue). |

## What is Flask?
Flask is a lightweight web framework in Python used for building web applications and APIs. It allows developers to define routes and handle HTTP requests with minimal setup.

### Example Flask API for JIRA Issue Creation
```python
from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth
import json
import os

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():
    API_TOKEN = os.getenv('JIRA_API_TOKEN')
    EMAIL = os.getenv('JIRA_EMAIL')
    
    if not API_TOKEN or not EMAIL:
        return json.dumps({"error": "Missing JIRA API credentials"}), 400
    
    url = "https://yourdomain.atlassian.net/rest/api/3/issue"
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "project": {"key": "PROJ"},
            "summary": "GitHub Event Triggered Issue",
            "description": "Issue automatically created from GitHub event.",
            "issuetype": {"name": "Task"}
        }
    })

    response = requests.post(url, headers=headers, auth=auth, data=payload)
    return json.dumps(json.loads(response.text), indent=4)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

## What is a Decorator in Python?
A decorator in Python is a function that modifies the behavior of another function without changing its structure. Flask uses decorators to define routes.

### Example of a Decorator in Flask:
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')  # This is a decorator
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run()
```
Here, `@app.route('/')` is a **decorator** that maps the `/` route to the `home` function.

## Conclusion
By automating JIRA issue creation based on GitHub events, teams can streamline their workflow and improve tracking of development progress.

---

**[Insert Screenshot Locations from Document]**
- Creating GitHub Webhook
- Copying EC2 Public IPv4 DNS
- Creating Issue and Commenting `/Jira`
- Verifying Issue in JIRA

