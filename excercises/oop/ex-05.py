"""
Modify the class you developed previously: add a method to create a dictionary with the attributes of
the sensor and to print them
"""

from datetime import date


class TemperatureSensor:
    def __init__(self, sensorName, sensorID, yearFabrication, isCalibrated):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.yearFabrication = yearFabrication
        self.isSensorCalibrated = isCalibrated
        self.measurements = []

    def show_info(self):
        print(f"Sensor ID:{self.sensorID}; Sensor Name: {self.sensorName}")

    def age(self):
        # current_date=input("Please Enter Today's Date (year): ")
        # current_date=int(current_date)
        current_date = date.today().year
        age_to_return = current_date - self.yearFabrication
        print(f"Sensor Age: {age_to_return}")

    def save(self, fileName, sensorName, sensorID, yearFabrication):
        f = open(f"excercises/{fileName}.txt", "w")
        f.write(f"{sensorName}, {sensorID}, {yearFabrication}")
        f.close()

    def isCalibrated(self):
        if self.isSensorCalibrated:
            print("The sensor is calibrated")
        else:
            print("The sensor is not calibrated")

    def readMeasuraments(self, fileName):
        fileContent = open(f"excercises/{fileName}.txt").read()
        measurements_list = fileContent.split(",")
        measurements_list_numbers = []
        for item in measurements_list:
            measurement = float(item)
            measurements_list_numbers.append(measurement)
        self.measurements = measurements_list_numbers

    def statistics(self):
        max_measurements = max(self.measurements)
        min_measurements = min(self.measurements)
        sum_measurements = 0
        count = 0
        for item in self.measurements:
            sum_measurements += item
            count += 1
        average_measurements = sum_measurements / count
        print(f"Measurements Average: {average_measurements}")
        print(f"Measurements Maximum: {max_measurements}")
        print(f"Measurements Minimum: {min_measurements}")

    def asDictionary(self):
        dictionary = {
            "SensorName": self.sensorName,
            "SensorID": self.sensorID,
            "YearOfCalibration": self.yearFabrication,
            "Measurements": self.measurements,
        }
        print(dictionary)


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
    instance_sensor.readMeasuraments("sensor1Measurements")
    instance_sensor.statistics()
    instance_sensor.asDictionary()
