# Get pull requests information on a git repo using python


import requests  #install requests module (pip install requests)

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")  #get the api from GitHub Docs

complete_detail = response.json() # this line of code converts the JSON response from an HTTP request into a Python dictionary

print(complete_detail[0]["user"]["id"])