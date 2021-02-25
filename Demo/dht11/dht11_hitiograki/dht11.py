# Raspberry Pi reads temperature and humidity sensor data from Arduino
import serial

# ef við þurfum að nota breadboard á RPi
# import RPi.GPIO as GPIO  

# This may change in your case to /dev/ttyUSB1, /dev/ttyUSB2, etc.
ser = serial.Serial('/dev/ttyACM0', 9600) # change ACM number as found from ls /dev/tty/ACM*

while True:
        # If serial data is present
        if ser.in_waiting > 0:
            #  read the line
            rawserial = ser.readline()
            #  decode() decodes the UTF8 data, convert byte strings to Unicode
            #  strip() removes the trailing end of line characters
            cookedserial = rawserial.decode('utf-8').strip('\r\n')
            #  split the data into temperature and humidity
            datasplit = cookedserial.split(',')
            #  remove the starting and ending pointers (< >)
            temperature = datasplit[0].strip('<')
            humidity = datasplit[1].strip('>')
            #  print the output in python console.
            print(temperature)
            print(humidity)
