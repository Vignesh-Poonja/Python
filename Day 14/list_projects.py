# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://poonjavigneshk.atlassian.net/rest/api/3/project"


auth = HTTPBasicAuth("poonjavigneshk@gmail.com", "ATATT3xFfGF0awlFYA5l0qVr3X6u5pdCV7fcPQprIS8ovjiUgFEVDfOcG26nWJPbvlkTNOP6SNqQIJGaigvRznJqRtvLsv3MRLPuul-iX-1NNRaheoTP7mlDFpHFdEjzniBK5OjoUqpv_kxf10pIJ6at0eqsH--JZDm1C32Y_Fv-4U0B6D-vvJ4=A31B9807")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#output = json.loads(response.text)  # Assuming response.text contains a valid JSON string

#name = output[0]["name"] 
 

# Using for loop to print all the project.

output = json.loads(response.text)

for item in output:  # Loop over the list, not its indices
    name = item["name"]  # Access "name" directly from each dictionary

print(name)
