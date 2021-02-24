
#### 3.2
Python kóði
```python
#! /bin/env python
import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

while True:
        read_ser=ser.readline()
        msg = read_ser.decode('utf-8')
        print(msg)
        if(msg.strip()=="Hello From Arduino!"):
              blink(11)

```
Arduino kóði
```c
String data="Hello From Arduino!";

void setup() {
Serial.begin(9600);

}

void loop() {
Serial.println(data);
delay(200);
}
```

#### 3.3
Python kóði
```python
#! /bin/env python

import serial
import time
ser =serial.Serial('/dev/ttyACM0',9600)

for i in range(21):
        ser.write(str.encode('3'))
        time.sleep(1)
        ser.write(str.encode('5'))
        time.sleep(2)
        ser.write(str.encode('6'))
        time.sleep(3)

```
Arduino kóði
```C
char receivedChar;
boolean newData = false;

void setup() {

  Serial.begin(9600);

  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);

}

void loop() {

  recvInfo();
  lightLED();

}

void recvInfo() {

  if (Serial.available() > 0) {

    receivedChar = Serial.read();
    newData = true;
   }
}

void lightLED() {

  int led = (receivedChar - '0');

  while(newData == true) {

    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);

```
