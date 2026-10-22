import json
import requests


class DeviceManager:  #class to retirve all the resources 

    def __init__(self, url):
        self.url = url

    def all(self):
        r = requests.get(self.url + "/all")
        output = r.json()
        return json.dumps(output, indent=4)

    def devices(self):
        r = requests.get(self.url + "/devices")
        output = r.json()
        return json.dumps(output, indent=4)

    def houses(self):
        r = requests.get(self.url + "/houses")
        output = r.json()
        return json.dumps(output, indent=4)

    def users(self):
        r = requests.get(self.url + "/users")
        output = r.json()
        return json.dumps(output, indent=4)


def menu(manager): #class to retrive info without restarting

    while True:
        command = input(
            "Select: all, devices, houses, users, quit: "
        ).strip().lower()

        output = "Command not found"

        if command == "all":
            output = manager.all()

        elif command == "devices":
            output = manager.devices()

        elif command == "houses":
            output = manager.houses()

        elif command == "users":
            output = manager.users()

        elif command == "quit":
            break

        print(output)


if __name__ == "__main__":

    manager = DeviceManager(
        "https://catalog-p4iot.onrender.com"
    )

    menu(manager)
