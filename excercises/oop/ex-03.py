"""
Modify the class you wrote for the previous exercise by adding one boolean attribute (i.e. True/False)
named isCalibrated, which should be provided by the user as input. Add also one method to assess
whether the sensor is calibrated or not.
"""

from datetime import date


class TemperatureSensor:
    def __init__(self, sensorName, sensorID, yearFabrication, isCalibrated):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.yearFabrication = yearFabrication
        self.isSensorCalibrated = isCalibrated

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

    def isCalibrated(self):
        if self.isSensorCalibrated:
            print("The sensor is calibrated")
        else:
            print("The sensor is not calibrated")


if __name__ == "__main__":
    usr_sensor_name = input("Please insert Sensor Name: ")
    usr_sensor_ID = input("Please insert Sensor ID: ")
    usr_year_fabrication = int(input("Please insert year of fabrication: "))
    usr_is_calibrated = input("Please insert the calibration: ")
    if usr_is_calibrated.lower() == "y" or usr_is_calibrated.lower() == "yes":
        sensor_calibration_bool = True
    elif usr_is_calibrated.lower() == "n" or usr_is_calibrated.lower() == "no":
        sensor_calibration_bool = False
    else:
        print("Input Error")
        raise ValueError
    instance_sensor = TemperatureSensor(
        usr_sensor_name, usr_sensor_ID, usr_year_fabrication, sensor_calibration_bool
    )
    instance_sensor.show_info()
    instance_sensor.age()
    # instance_sensor.save("myFile", usr_sensor_name, usr_sensor_ID, usr_year_fabrication, usr_is_Calibrated)
    instance_sensor.isCalibrated()
