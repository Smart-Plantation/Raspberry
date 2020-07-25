import requests
from datetime import datetime
r = requests.get('https://smart-plantation.herokuapp.com/status')
print(r.status_code)
with open('/home/pi/Documents/Smart-Plantation/Raspberry/logs/log_get.txt','a') as log:
    log.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Status: ' + str(r.status_code) + ' - ' + r.reason + '\n')