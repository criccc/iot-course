import json
import requests

url = "https://catalog-p4iot.onrender.com"

resource = "/devices"

r = requests.get(url + resource)

output = r.json() #convert json to the python dictionary 

print(json.dumps(output, indent=4)) #converts to the nicely json format
