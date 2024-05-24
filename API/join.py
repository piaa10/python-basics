import requests
import json

url = "https://xx.xx.xxx.com/service/rest/v1/components?repository=docker"
response = requests.get(url)
dict = response.json()
token = dict.get("continuationToken")
list = ""
num = 0

while token != 'null' and token != 123:
    current_url = f"{url}&continuationToken={token}"
    response = requests.get(current_url)
    try:
        dict = response.json()
    except json.decoder.JSONDecodeError:
        print("No more data available.")
        break
    token = dict.get("continuationToken")
    list = dict["items"]
    for lists in list:
        print(lists["name"])
