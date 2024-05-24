import requests

url = "https://registry.production.xxx.com/service/rest/v1/components?repository=docker"
response = requests.get(url)
dict = response.json()
token = dict.get("continuationToken")

while token != 'null' and token != 123:
    current_url = f"{url}&continuationToken={token}"
    response = requests.get(current_url)
    dict = response.json()
    token = dict.get("continuationToken")
    print(token)
