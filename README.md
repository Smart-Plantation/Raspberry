# Raspberry

## How to configure

### Module get_service_data.py

1. Crontab -e
2. */20 * * * * python3 /home/pi/Documents/Smart-Plantation/Raspberry/get_service_data.py
   0 * * * * python3 /home/pi/Documents/Smart-Plantation/Raspberry/post_data.py

