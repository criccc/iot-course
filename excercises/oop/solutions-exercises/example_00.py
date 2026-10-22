class TemperatureSensor:
    def __init__(self,sensorName,sensorID):
        self.sensorName=sensorName
        self.sensorID=sensorID
    def show_sensorID(self):
        print(f"sID {self.sensorID}, sName {self.sensorName}")

#This is the main of our program
if __name__=="__main__":
    sensorName="DHT11"
    sensorID="s-001"
    sensor1= TemperatureSensor(sensorName,sensorID)
    sensor1.show_sensorID()