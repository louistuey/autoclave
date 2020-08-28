import adafruit_ds3231
import busio
import time

from board import *

myi2c = busio.I2C(SCL,SDA)
rtc = adafruit_ds3231.DS3231(myi2c)

# rtc.datetime = time.struct_time((2020,8,27,19,41,0,0,9,0))
#struct_time((year,mon,day,hour{24},min,sec,weekday,0?,0?))
t = rtc.datetime
print("Date: " ,t.tm_year,"-",t.tm_mon,"-",t.tm_mday)
print("Time= ",t.tm_hour, " : ", t.tm_min)
print(t.tm_wday)