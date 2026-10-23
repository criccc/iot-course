"""
Develop in OOP a program for managing a list of devices The full list of devices is
stored in the file “catalog.json” (available at this link)
The program needs to load the file and manage the catalog, providing the following
features:
    • searchByName: print all the information about the devices for the given
    • searchByID: print all the information about the devices for the given
    • searchByService: print all the information about the devices that provides the
    given
    • searchByMeasureType: print all the information about the device that
    provides such measure
    • insertDevice: insert a new device it that is not already present on the list (the
    ID is checked). Otherwise ask the end-user to update the information about the
    existing device with the new parameters. Every time that this operation is
    performed the “last_update” field needs to be updated with the current date and
    time in the format “yyyy-mm-dd hh:mm”. The structure of the parameters of
    the file must follow the one of the ones that are already present
    • printAll: print the full catalog
    • exit: save the catalog (if changed) in the same JSON file provided as input.
Finally, once the update file has been saved, validate the new JSON with jsonlint
(http://jsonlint.com/)
"""

import json
from datetime import date


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
        user_input_id = input("Enter the desired Device ID: ")
        devices_list = self.catalog["devicesList"]
        
        devices_found = []
        found = False
        
        for device in devices_list:
            if device["deviceID"] == user_input_id:
                devices_found.append(device)
                found = True
        
        if found:
            print(devices_found)
        else:
            print("No Devices found with that ID")
        return

    def printAll(self):
        print(json.dumps(self.catalog, indent=2))

    def insertDevice(self):
        user_input_id = input("Enter the new Device ID: ")
        devices_list = self.catalog["devicesList"]
        found = False
        for device in devices_list:
            if device["deviceID"] == user_input_id:
                found = True
                break
        if found:
            print("The ID inserted already exists.")
            answer = input("Do you want to update this device? (y/n) ")
            if answer == "y":
                device["deviceName"] = input("Please enter the new Device Name:")
                new_services = []
                while True:
                    service_to_enter = input(
                        "Please add the serviceName available. When finish type 'ok' "
                    )
                    if service_to_enter == "ok":
                        break
                    else:
                        new_services.append(service_to_enter)
                device["availableServices"] = new_services
                device["lastUpdate"] = date.now().strftime("%Y-%m-%d %H:%M")
                self.catalog["lastUpdate"] = device["lastUpdate"]
                self.changed = True
        else:
            user_input_name = input("Please enter the Device Name:")
            available_services = []
            while True:
                service_to_enter = input(
                    "Please add the serviceName available. When finish type 'ok' "
                )
                if service_to_enter == "ok":
                    break
                else:
                    available_services.append(service_to_enter)
            measure_types = []
            while True:
                measure = input("Please add the measureType. When finish type 'ok' ")
                if measure == "ok":
                    break
                else:
                    measure_types.append(measure)
            services_details = []
            for service in available_services:
                if service == "MQTT":
                    topics = []
                    while True:
                        topic = input("Please add a topic. When finish type 'ok' ")
                        if topic == "ok":
                            break
                        else:
                            topics.append(topic)
                    services_details.append({"serviceType": "MQTT", "topic": topics})
                elif service == "REST":
                    ip = input("Please enter the serviceIP: ")
                    services_details.append({"serviceType": "REST", "serviceIP": ip})
            device_dict = {
                "deviceName": user_input_name,
                "deviceID": user_input_id,
                "availableServices": available_services,
                "measureType": measure_types,
                "servicesDetails": services_details,
                "lastUpdate": date.now().strftime("%Y-%m-%d %H:%M"),
            }
            self.catalog["devicesList"].append(device_dict)
            self.catalog["lastUpdate"] = device_dict["lastUpdate"]
            self.changed = True
            json.dump(self.catalog, open("catalog.json", "w"))


if __name__ == "__main__":
    welcome_message = "Hello, welcome to the Device Manager."
    available_actions_message = (
        "The available actions are: \n 'sName' to search by name  \n"
        " 'sID' to search by ID \n"
        " 'sService' to search by service \n"
        " 'sMeasure' to search by measure type \n"
        " 'insert' to insert a device \n"
        " 'printAll' to print the full catalog \n"
        " 'e' exit"
    )
    condition_iterate = True
    device_manager_instance = DeviceManager()
    print(welcome_message)
    while True:
        print(available_actions_message)
        user_input = input("\n Please enter the action to be performed: ")
        if user_input == "sName":
            device_manager_instance.searchByName()
        elif user_input == "sID":
            device_manager_instance.searchByID()
        elif user_input == "sService":
            device_manager_instance.searchByService()
        elif user_input == "sMeasure":
            device_manager_instance.searchByMeasureType()
        elif user_input == "insert":
            device_manager_instance.insertDevice()
        elif user_input == "printAll":
            device_manager_instance.printAll()
        elif user_input == "e" or user_input == "exit":
            device_manager_instance.exit()
            condition_iterate = False
            break
