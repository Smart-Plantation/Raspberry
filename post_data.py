import serial
import requests
from datetime import datetime

temperature = None
moisture = None
watering = None

serial_interface = serial.Serial("/dev/ttyUSB0",9600)
serial_interface.baudrate = 9600
if datetime.now().hour == 16:
    print('regar')
    serial_interface.write(b'b')
else:
    print('n regar')
    serial_interface.write(b'a')

serial_data = serial_interface.readline().decode().strip().split()
print(serial_data)

temperature, moisture, watering = serial_data
print("Temp: " + temperature)
print("Moist: " + moisture)
print("Watering: " + watering)
        
r = requests.post('https://smart-plantation.herokuapp.com/data',params = {'temperature':temperature,'moisture':moisture,'watering':watering})

with open('/home/pi/Documents/Smart-Plantation/Raspberry/logs/log_post.txt','a') as log:
    log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Temp: ' + str(temperature) + ' Moist: ' + moisture + ' Water: ' + watering + ' Request Status: ' + str(r.status_code) + ' - ' + r.reason + '\n')
    
#r = requests.post('http://0.0.0.0:5000/data',params = {'temperature':temperature,'moisture':moisture,'watering':watering})
#print(r.status_code)
