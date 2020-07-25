import serial
import requests
from datetime import datetime
from time import sleep

def request_data_from_serial():
    if now.hour == 16:
        print('Water and retrieve data')
        serial_interface.write(b'b')
    else:
        print('Retrieve data')
        serial_interface.write(b'a')

temperature = None
moisture = None
watering = None

LOG_PATH = '/home/pi/Documents/Smart-Plantation/Raspberry/logs/log_post.txt'
APP_URL = 'https://smart-plantation.herokuapp.com/data'

serial_interface = serial.Serial("/dev/ttyUSB0",9600, timeout=3)
now = datetime.now()
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
    
try:
    #First read is dummy
    serial_interface.write(b'a')
    serial_interface.read()
    sleep(0.2)

    request_data_from_serial()

    temperature, moisture, watering = serial_interface.readline().decode().strip().split()
    print(temperature, moisture, watering)
except:
    with open(LOG_PATH,'a') as log:
        log.write(timestamp + ' Unable to retrieve data from serial')
    exit(1)
       
r = requests.post(APP_URL,params = {'temperature':temperature,'moisture':moisture,'watering':watering})

with open(LOG_PATH,'a') as log:
    log.write(timestamp + ' Temp: ' + str(temperature) + ' Moist: ' + moisture + ' Water: ' + watering + ' Request Status: ' + str(r.status_code) + ' - ' + r.reason + '\n')