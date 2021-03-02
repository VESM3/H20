### V4.1
```python

"""

Example of sending button values to an Adafruit IO feed.
Author(s): Gunnar Þórunnarson

"""

# import standard python modules
import time

# import RPi.GPIO 
import RPi.GPIO as GPIO

# import Adafruit IO 
from Adafruit_IO import *    

# Set to your Adafruit IO key.
ADAFRUIT_IO_KEY = ''

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = ''

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Pin setup 
GPIO.setmode(GPIO.BCM)

# hnappur með viðnám
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# upphafsstaða
button_current = 0       

try:
    while True:
        if not GPIO.input(12):
            button_current = 1
        else:
            button_current = 0
            
        print('Button -> ', button_current)
    
        # send data to feed
        aio.send("digital3", button_current)

        # avoid timeout from adafruit io
        time.sleep(1)
    
finally:
    # this ensures a clean exit
    # https://raspi.tv/2013/rpi-gpio-basics-3-how-to-exit-gpio-programs-cleanly-avoid-warnings-and-protect-your-pi
    GPIO.cleanup() 
```
### V4.2

```python
"""
kveikja á led peru með ON/OFF takki í Dashboard á Adafruit IO 
"""

#importa time
import time

#importa GPIO modulei
import RPi.GPIO as GPIO

#importa öllu frá adafruit io
from Adafruit_IO import *

#lykill skilgreindur
ADAFRUIT_IO_KEY = ''

#notandanafn skilgreint
ADAFRUIT_IO_USERNAME = ''

#client skilgreindur með lykli og notandanafni
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#prófa að fá digital feed
try:
    digital = aio.feeds('digital')
#ef að villa kemur upp þá skilgreina það manually
except RequestError:
    feed = Feed(name="digital")
    digital = aio.create_feed(feed)

#set warnings ignorar alla warnings
GPIO.setwarnings(False)
#setmode BCM
GPIO.setmode(GPIO.BCM)
#pinni 15 sem output fyrir led ljós
GPIO.setup(15,GPIO.OUT)

#keyrir endalaust
while True:
    #data = lykill sem er móttekinn
    data = aio.receive(digital.key)
    #ef að value er 1
    if int(data.value) == 1:
        #þá fer hann on
        print('received <- ON\n')
    #annars off
    elif int(data.value) == 0:
        print('received <- OFF\n')
    #outpinni er breytuheiti yfir GPIO outputtið sem breytist eftir hvaða gildi kemur frá server, þarf svo sem ekki að vera heiti
    outPinni = GPIO.output(15,int(data.value))
    #sefur í hálfa sek til að koma í veg fyrir timeout á serverinn
    time.sleep(0.5)

```
