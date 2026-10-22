"""
Modify the class you wrote for the previous exercise (ex-01.py) by adding a method that writes the Sensor
information on a .txt file
"""

from datetime import date


class TemperatureSensor:
    def __init__(self, sensorName, sensorID, yearFabrication):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.yearFabrication = yearFabrication

    def show_info(self):
        print(f"Sensor ID:{self.sensorID}; Sensor Name: {self.sensorName}")

    def age(self):
        # current_date=input("Please Enter Today's Date (year): ")
        # current_date=int(current_date)
        current_date = date.today().year
        age_to_return = current_date - self.yearFabrication
        print(f"Sensor Age: {age_to_return}")

    def save(self, file_name, sensorName, sensorID, yearFabrication):
        f = open(f"excercises/{file_name}.txt", "w")
        f.write(f"{sensorName}, {sensorID}, {yearFabrication}")
        f.close()


if __name__ == "__main__":
    usr_sensor_name = input("Please insert Sensor Name: ")
    usr_sensor_ID = input("Please insert Sensor ID: ")
    usr_year_fabrication = int(input("Please insert year of fabrication: "))
    instance_sensor = TemperatureSensor(
        usr_sensor_name, usr_sensor_ID, usr_year_fabrication
    )
    instance_sensor.show_info()
    instance_sensor.age()
    instance_sensor.save("myFile", usr_sensor_name, usr_sensor_ID, usr_year_fabrication)
