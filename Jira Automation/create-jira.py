# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
import os


# Use environment variables for sensitive information
API_TOKEN = os.getenv('JIRA_API_TOKEN')
EMAIL = os.getenv('JIRA_EMAIL')


url = "https://poonjavigneshk.atlassian.net/rest/api/3/issue"

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10003"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
})

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

if response.status_code == 201:
    print("Issue created successfully.")
    print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)