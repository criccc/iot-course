'''
Modify the code of exercise 4 and 5 to be able to work with a json file similar to the one below:
('temperatureSensor.json')
{
“sensorID”: ”s-001”,
”sensorName”: ”DHT11”,
”yearFabrication”: 2022,
”calibrated”: “yes”
}
'''

from datetime import date
import json


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
    json_file_content = json.load(open('excercises/temperatureSensor.json'))
    instance_sensor = TemperatureSensor(
        json_file_content["sensorName"], json_file_content["sensorID"], json_file_content["yearFabrication"], json_file_content["calibrated"]
    )
    instance_sensor.show_info()
    instance_sensor.age()
    # instance_sensor.save("myFile", usr_sensor_name, usr_sensor_ID, usr_year_fabrication, usr_is_Calibrated)
    instance_sensor.isCalibrated()
    instance_sensor.readMeasuraments("sensor1Measurements") 
    instance_sensor.statistics()
    instance_sensor.asDictionary()
