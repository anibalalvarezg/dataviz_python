import requests

response = requests.get("https://en.wikipedia.org/wiki/Nobel_Prize")

#print(dir(response))

#print(response.status_code)
#print(response)
print(response.text)
