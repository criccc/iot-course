"""
Develop a Sensor class similar to the one in the previous example. The class should be able to receive as
input the sensor name, the sensor ID and the year of fabrication of the sensor. In addition, it must have
a method to return the current “age” of the sensor. The input should be provided by the user (NOT
hardcoded in the script).
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


if __name__ == "__main__":
    usr_sensor_name = input("Please insert Sensor Name: ")
    usr_sensor_ID = input("Please insert Sensor ID: ")
    usr_year_fabrication = int(input("Please insert year of fabrication: "))
    instance_sensor = TemperatureSensor(
        usr_sensor_name, usr_sensor_ID, usr_year_fabrication
    )
    instance_sensor.show_info()
    instance_sensor.age()
