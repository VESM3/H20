## Soil sensor

---

### Tutorials
- [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor](https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/overview)
- [How to Use a Soil Moisture Sensor to Keep Your Plants Alive (with python)](https://medium.com/initial-state/how-to-use-a-soil-moisture-sensor-to-keep-your-plants-alive-51a2294b88e)
- [Testing Capacitive soil moisture sensors](https://flashgamer.com/blog/comments/testing-capacitive-soil-moisture-sensors)


### adafruit_seesaw safnið
- [arduino](https://adafruit.github.io/Adafruit_Seesaw/html/class_adafruit__seesaw.html)
- [python](https://circuitpython.readthedocs.io/projects/seesaw/en/latest/api.html#adafruit-seesaw-seesaw)


### Kóðasýnidæmi

Arduino

```C
#include "Adafruit_seesaw.h"

Adafruit_seesaw ss;

void setup() {
  Serial.begin(115200);

  Serial.println("seesaw Soil Sensor example!");
  
  if (!ss.begin(0x36)) {
    Serial.println("ERROR! seesaw not found");
    while(1);
  } else {
    Serial.print("seesaw started! version: ");
    Serial.println(ss.getVersion(), HEX);
  }
}

void loop() {
  float tempC = ss.getTemp();
  uint16_t capread = ss.touchRead(0);

  Serial.print("Temperature: "); Serial.print(tempC); Serial.println("*C");
  Serial.print("Capacitive: "); Serial.println(capread);
  delay(100);
}
```

Python
```python
import time
 
from board import SCL, SDA
import busio
 
from adafruit_seesaw.seesaw import Seesaw
 
i2c_bus = busio.I2C(SCL, SDA)
 
ss = Seesaw(i2c_bus, addr=0x36)
 
while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
 
    # read temperature from the temperature sensor
    temp = ss.get_temp()
 
    print("temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)
```

