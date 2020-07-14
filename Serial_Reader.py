import serial
import requests
import time

temperature = None
moisture = None
watering = None

while(1):
	serial_interface = serial.Serial("/dev/ttyUSB0",9600)
	serial_interface.baudrate = 9600
	time.sleep(3)
	serial_interface.write(b'a')

	serial_data = serial_interface.readline().rstrip().split(" ")

	temperature, moisture, watering = serial_data
	print("Temp: " + temperature)
	print("Moist: " + moisture)
	print("Watering: " + watering)
        
		    
	##r = requests.post('https://smart-plantation.herokuapp.com/data',params = {'temperature':temperature,'moisture':moisture,'watering':watering})
	#r = requests.post('http://0.0.0.0:5000/data',params = {'temperature':temperature,'moisture':moisture,'watering':watering})
	#print(r.status_code)
