from datetime import date
import json

class TemperatureSensor:
    def __init__(self,sensorName,sensorID,yearFabrication, calibrationBool):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.yearFabrication = yearFabrication
        self.sensorCalibration = calibrationBool
    
    def show_info(self):
        print(f'SensorID: {self.sensorID}; SensorName: {self.sensorName} ')
    
    def age(self):
        #current_date=input("Please Enter Today's date (year):")
        #current_date=int(current_date)
        current_date=date.today().year
        age_to_return=current_date-self.yearFabrication
        print(f'Sensor Age: {age_to_return}')
    
    def save(self):
        usr_file_name=input('Please enter the file name: ')
        file_to_open=open(f'{usr_file_name}.txt','w')
        to_write=f'{self.sensorName}, {self.sensorID}, {self.yearFabrication}'
        #to_write=self.sensorName+','+self.sensorID+','+self.yearFabrication
        file_to_open.write(to_write)
        file_to_open.close()
    
    def isCalibrated(self):
        if self.sensorCalibration:
            print("The sensor is calibrated")
        else:
            print("The sensor is NOT calibrated")
    
    def readMeasurements(self):
        measurements_file_name="sensor1_measurements.txt"
        file_object=open(measurements_file_name).read()
        measurements_list=file_object.split(',')
        print(measurements_list)
        #convert strings into numbers
        measurements_list_numbers=[]
        for item in measurements_list:
            measurement = float(item)
            measurements_list_numbers.append(measurement)
            #measurements_list_numbers.append(float(item))
        self.measurements= measurements_list_numbers
    
    def statistics(self):
        min_measure=min(self.measurements)
        max_measure=max(self.measurements)
        sum_measurements=0
        count=0
        for item in self.measurements:
            sum_measurements+=item
            # sum_measurements= sum_measurements+item
            count+=1
            #count= count+1
        average_measurements= sum_measurements/count
        print(f'Min measure: {min_measure}')
        print(f'Max Measure: {max_measure}')
        print(f'Average: {average_measurements}')

    def asDictionary(self):
        sensor_dict={
            'sensorID': self.sensorID,
            'sensorName': self.sensorName,
            'yearFabrication': self.yearFabrication,
            'measurements': self.measurements
        }
        #return sensor_dict
        print(sensor_dict)
    
if __name__ == "__main__":
    #usr_sensor_name=input("Please insert Sensor Name: ")
    #usr_sensor_id=input("Please insert Sensor ID:")
    #usr_year_fabrication=int(input("Please insert year of fabrication: "))
    '''
    Load sensor configuration from configuration file rather than user input
    '''
    configuration_sensor_file=json.load(open('temperatureSensor.json'))
    usr_sensor_name=configuration_sensor_file['sensorName']
    usr_sensor_id=configuration_sensor_file['sensorID']
    usr_year_fabrication=configuration_sensor_file['yearFabrication']
    usr_sensor_calibration=configuration_sensor_file['calibrated']
    if usr_sensor_calibration=='y' or usr_sensor_calibration=='yes':
        sensor_calibration_bool=True
    elif usr_sensor_calibration=='n' or usr_sensor_calibration=='no':
        sensor_calibration_bool=False
    else:
        print("Wrong input")
        raise ValueError
    instance_sensor= TemperatureSensor(usr_sensor_name, usr_sensor_id, usr_year_fabrication, sensor_calibration_bool)
    instance_sensor.show_info()
    instance_sensor.age()
    instance_sensor.save()
    instance_sensor.isCalibrated()
    instance_sensor.readMeasurements()
    instance_sensor.statistics()
    instance_sensor.asDictionary()
