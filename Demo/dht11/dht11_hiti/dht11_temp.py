# Raspberry Pi reads temperature and humidity sensor data from Arduino
import serial

# change ACM number as found from ls /dev/tty/ACM*
ser = serial.Serial('/dev/ttyACM0', 9600) 
while True:
        # If serial data is present
        if ser.in_waiting > 0:
            #  read the line
            rawserial = ser.readline()
            #  decode() decodes the UTF8 data, convert byte strings to Unicode
            #  strip() removes the trailing end of line characters
            # temp = rawserial.decode('utf-8').strip('\r\n')
            temperature = rawserial.decode('utf-8').strip()
            #  print the output in python console.
            print(temperature)
      
