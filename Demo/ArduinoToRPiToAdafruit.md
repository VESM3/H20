##  Gagnaflutningir Arduino->RPi->Adafruit
Hvert "send" tekur nokkrar sekúndur.

### Arduino kóði
```C
float tala1;
float tala2;
float tala3; 

void setup() {
  Serial.begin(9600); 
  randomSeed(A0);
} 

void loop() {
  tala1 = float(random(1000) + 100)/10.0;
  tala2 = float(random(1000) + 100)/10.0;
  tala3 = float(random(1000) + 100)/10.0;
  Serial.print(tala1);
  Serial.print(",");
  Serial.print(tala2);
  Serial.print(",");
  Serial.println(tala3);
  delay(1000);
}
```

### Python kóði

```python
import serial
import time
from Adafruit_IO import Client, Feed, RequestError 

ser = serial.Serial('/dev/ttyACM0',9600) # ATH getur verið öðruvísi fyri Pi zero

ADAFRUIT_IO_USERNAME = "notendanafn"
ADAFRUIT_IO_KEY = "lykill" 

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY) 

FEEDS = ["feed1", "feed2", "feed3"] # nöfnin á Feed-unum á Adafruit IO 

while True:
    try:
        fra_arduino = ser.readline().decode("utf-8") # Fáum 3 gildi í einum streng 
                                                     # t.d. "1.23, 2.34, 3.45"
        gildi1 = fra_arduino.split(",")[0]
        gildi2 = fra_arduino.split(",")[1]
        gildi3 = fra_arduino.split(",")[2] 

        aio.send(FEEDS[0], gildi1)
        aio.send(FEEDS[1], gildi2)
        aio.send(FEEDS[2], gildi3)
    
        time.sleep(10) # sendum á 10 sek. fresti
    except IndexError:
        # grípum villu ef við fáum eitthvað annað frá Arduino en við eigum von á
        print("Óvænt gildi frá Arduino!!")
```
