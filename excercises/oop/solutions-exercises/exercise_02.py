from datetime import date

class TemperatureSensor:
    def __init__(self,sensorName,sensorID,yearFabrication):
        self.sensorName = sensorName
        self.sensorID = sensorID
        self.yearFabrication = yearFabrication
    
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

if __name__ == "__main__":
    usr_sensor_name=input("Please insert Sensor Name: ")
    usr_sensor_id=input("Please insert Sensor ID:")
    usr_year_fabrication=int(input("Please insert year of fabrication: "))
    instance_sensor= TemperatureSensor(usr_sensor_name, usr_sensor_id, usr_year_fabrication)
    instance_sensor.show_info()
    instance_sensor.age()
    instance_sensor.save()