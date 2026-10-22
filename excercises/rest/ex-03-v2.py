
import json
import requests

url = "https://catalog-p4iot.onrender.com"

command = input("Select: all, devices, houses, users: ") 

if command == "all":
    resource = "/all"

elif command == "devices":
    resource = "/devices"

elif command == "houses":
    resource = "/houses"

elif command == "users":
    resource = "/users"

else:
    resource = None

if resource is not None:
    r = requests.get(url + resource)
    output = r.json()
    print(json.dumps(output, indent=4))

else:
    print("Command not found")
