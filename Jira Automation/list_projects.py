# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://poonjavigneshk.atlassian.net/rest/api/3/project"

API_TOKEN=""
EMAIL=""

auth = HTTPBasicAuth(EMAIL, API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text) # Parse the JSON response text into a Python dictionary

name = output[0]["name"] # Extract the name of the first project from the JSON response

print(name) # Print the name of the first project
