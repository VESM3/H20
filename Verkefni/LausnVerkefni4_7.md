### V4.7

- Sendu analog gildi frá ljósviðnámi (e. photocell) til Adafruit IO. 
- Birtu rauntímaniðurstöður með Gauge block og línuriti í Dashboard.
- Notaðu Arduino og RaspberryPi saman til að leysa verkefnið. Arduino á að sjá um að mæla gildin.

**Arduion kóði**

```c

#define PHOTOCELL_PIN A0

int current = 0;
int last = -1;

void setup() {
  Serial.begin(9600);
  
  while(! Serial);
  
  Serial.print("Connecting...");
  Serial.println();
}

void loop() {
  delay(2000);
  
  current = analogRead(PHOTOCELL_PIN);
  
  if(current == last)
    return;
  
  Serial.print("");
  Serial.println(current);
  
  last = current;
  
  delay(100);
}

```
**RaspberryPi kóði**

```python
import time
import serial
from Adafruit_IO import *

ADAFRUIT_IO_KEY = ''

ADAFRUIT_IO_USERNAME = ''

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    analog = aio.feeds('analog')
except RequestError:
    feed = Feed(name='analog')
    analog = aio.create_feed(feed)
    
ser = serial.Serial('/dev/ttyACM1', 9600)

while True:
    lesaValue = ser.readline()
    value = lesaValue.decode('utf-8')
    print("Analog data ->",value)
    aio.send(analog.key, value)
    time.sleep(0.75)
    
```
