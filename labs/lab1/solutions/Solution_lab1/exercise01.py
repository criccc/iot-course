import json


class DeviceManager:
    def __init__(self):
        self.catalog = json.load(open("../lab1/catalog.json"))

    def searchByName(self):
        user_input_name = input("Enter the desired Device Name: ")
        devices_list = self.catalog["devicesList"]

        devices_found = []
        found = False

        for device in devices_list:
            if device["deviceName"] == user_input_name:
                devices_found.append(device)
                found = True

        if found:
            print(devices_found)
        else:
            print("No Devices found with that name")

    def searchById(self):
        # code
        return

    def printAll(self):
        # code
        return

    def insertDevice(self):
        user_input_id = input("Enter the new Device ID: ")
        devices_list = self.catalog["devicesList"]
        found = False
        for device in devices_list:
            if device["deviceID"] == user_input_id:
                found = True
                break
        if found:
            print(
                "The ID inserted already exists. Please check for adding a new device"
            )
        else:
            user_input_name = input("Please enter the Device Name:")
            # available_services
            available_services = []
            while True:
                service_to_enter = input(
                    "Please add the serviceName available. When finish type 'ok' "
                )
                if service_to_enter == "ok":
                    break
                else:
                    available_services.append(service_to_enter)
            # other code for the other attributes of the device
            #
            #
            #
            device_dict = {
                "deviceName": user_input_name,
                "deviceID": user_input_id,
                "availableServices": available_services,
            }
            self.catalog["devicesList"].append(device_dict)
            json.dump(self.catalog, open("catalog.json", "w"))


if __name__ == "__main__":
    welcome_message = "Hello, welcome to the Device Manager."
    available_actions_message = (
        "The available actions are: \n 'sName' to search by name  \n 'e' exit"
    )
    condition_iterate = True
    device_manager_instance = DeviceManager()
    print(welcome_message)
    while True:
        print(available_actions_message)
        user_input = input("\n Please enter the action to be performed: ")
        if user_input == "sName":
            device_manager_instance.searchByName()
        elif user_input == "e" or user_input == "exit":
            condition_iterate = False
            break
