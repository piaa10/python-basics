import requests

response = requests.get("https://xx.xx.xxx.com/service/rest/v1/components?repository=docker")
#print(type(response.json())) #dictionary

dict = response.json()
#print(dict["items"]) #list
list = dict["items"]
''''#print(type(list[0])) #dictionary
dict2 = list[0]
print(dict2["name"])'''

num = 0
while num <= 7:
    for lists in list:
        dic2 = list[num]
        num += 1
        print(dic2["name"])


