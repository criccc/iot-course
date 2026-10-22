import requests

url = "https://catalog-p4iot.onrender.com/all"

r = requests.get(url)

print(r.status_code) #the http response status
print(r.text)


