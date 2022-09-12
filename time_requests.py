import urequests
import time
import machine
from wifi import Wifi

def parse_light_time(utc_time, light_time):
    sun_clock = light_time[-3:].strip()
    light_time = light_time[:-3].split(':')
    light_time = [int(i) for i in light_time]
    light_utc_time = list(utc_time)
    light_utc_time[3] = light_time[0] if sun_clock == 'AM' else light_time[0] + 12
    light_utc_time[4] = light_time[1]
    light_utc_time[5] = light_time[2]

    return light_utc_time

def get_current_utc_time():
    Wifi.connect()

    response = urequests.get('http://worldtimeapi.org/api/timezone/Asia/Tokyo')

    utc_time = list(time.localtime(response.json()['unixtime']))
    utc_time[0] = utc_time[0] - 30 # minux 30 years cause unix time 1970-01-01, board 2000-01-01
    return utc_time

def get_light_on_off_time(utc_time):
    light_on_time = "1:00:00 PM" 
    print("light on time: "+light_on_time)
    light_off_time = "12:00:00 AM"
    print("light off time: "+light_off_time)

    return parse_light_time(utc_time, light_on_time), parse_light_time(utc_time, light_off_time)