#!/usr/bin/python3


from time import sleep, strftime, time
import board
import adafruit_ahtx0


i2c = board.I2C()                       # uses board.SCL and board.SDA
sensor = adafruit_ahtx0.AHTx0(i2c)      # The default I2C address is 0x38.
cpu = CPUTemperature()


with open("/home/nate/temp_humid.csv", "a") as log:
  while True:
    humid = round(sensor.relative_humidity, 1)
    temp_F = round((sensor.temperature * 1.8) + 32, 1)	# Temperature in F
    log.write("{0},{1}\n".format(strftime("%y-%m-%d %H:%M:%S"),str(temp_F)))
    sleep(1)


# print("Temperature: {}F, Humidity: {}%".format(temp_F, humid))

