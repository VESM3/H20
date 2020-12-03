### Verkefni 2 - Skynjarar (15%) 
Einstaklingsverkefni

---

1. Blikkandi ljós og GPIO **(3%)** <br>
Láttu LED blikka á brauðbretti með python kóða. Notaðu [RPi.GPIO](https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/) með BCM númerakerfinu. Sjá t.d. [blink tutorial (notar BOARD)](https://raspberrypihq.com/making-a-led-blink-using-the-raspberry-pi-and-python/)

1. PIR hreyfiskynjarinn **(4%)** <br>
Notaðu PIR hreyfisyknjara til að kveikja á LED.
    - [Nánar um PIR (ath víxlaðu GND og Vc í PIR)](https://learn.adafruit.com/pir-passive-infrared-proximity-motion-sensor/overview)
    - [How to Interface a PIR Motion Sensor With Raspberry Pi GPIO](https://maker.pro/raspberry-pi/tutorial/how-to-interface-a-pir-motion-sensor-with-raspberry-pi-gpio)
    - Yfirfarðu kóðann, tengdu víra rétt í PIR (finna datasheet), stilltu næmleika og timeout (hve lengi) á PIR, taktu linsu af PIR til að þrengja IR svið. 
   
1. Pi V2 Camera **(2%)** <br>
Notaðu python og taktu mynd með 1024x768 upplausn (eða hærri) af sjálfum þér með Pi NoIR V2 myndavélinni tengda við RPi.   
   - **Varúð!** Slökktu fyrst á RPi þegar þú tengir myndavélina við Camera Serial Interface (CSI) á RPi. 
   - Sjá tutorial [Setting up the Pi NoIR Camera with Raspberry Pi](https://maker.pro/raspberry-pi/tutorial/how-to-interface-pi-noir-v2-camera-with-raspberry-pi)
  
1. Pi V2 Camera **(2%)** <br>
Taktu 5 sekúndu myndband með Pi NoIR V2 myndavélinni tengda við RPi og python   
   - [PiCamera documentation](https://picamera.readthedocs.io/en/release-1.13/)

1. PIR og Pi Camera **(4%)** <br>
Taktu mynd þegar PIR hreyfiskynjari fer í gang og sendu ljósmyndina á gmail netfang.
    - [How to Use the Raspberry Pi4 Camera and PIR Sensor to Send Emails](https://maker.pro/raspberry-pi/projects/how-to-use-the-raspberry-pi4-camera-and-pir-sensor-to-send-emails)
    - Búðu til Gmail reikning og leyfðu “Allow less secure apps” svo hægt er að taka við tölvpóst með python kóða.
      
   <!-- 
   - Sjá líka [How to Use the Raspberry Pi Camera and PIR to Send Emails](https://maker.pro/raspberry-pi/tutorial/how-to-use-the-raspberry-pi-camera-to-send-emails)
   -->
---

### Námsmat
- Gefið er fyrir hvern þið fullt fyrir fullnægjandi lausn, hálft ef ábótavant.
- Skilaðu á Innu vefslóð á Wiki síðu á Github sem inniheldur lausnir, kóða og myndbönd af verklegum tilraunum.
