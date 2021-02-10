## Verkefni 3 -  IoT Samskipti (20%)

Einstaklingsverkefni<br>
Tími: 3 vikur

---

#### 3.1. Arduino og Raspberry Pi (1%)
  1. Hver er munurinn á Arduino Uno og Raspberry Pi, nefndu helstu atriði?
  1. Hver er munurinn á Arduino Uno og Arduino Nano IoT 33
  1. Hvenær og afhverju getur það verið gagnlegt að tengja Arduino og Raspberry Pi saman? Komdu með dæmi.
  
---

#### 3.2 Serial tenging, Arduino til RPi (2%)
Fylgdu tutorial: [How to Connect and Interface a Raspberry Pi With an Arduino](https://maker.pro/raspberry-pi/tutorial/how-to-connect-and-interface-raspberry-pi-with-arduino)
  - Láttu Arduino senda strenginn “Hello from Arduino” til Raspberry Pi. Raspberry Pi við móttöku prentar út strenginn og lætur LED blikka.
  - **Ath** Laga þarf kóðann í tutorialnum `if` skilar ekki `True`. Hér er lagfærður kóði með decode() og strip(): 
  
    ```
    while True:

      read_ser=ser.readline()
      msg = read_ser.decode('utf-8') # To convert byte strings to Unicode, líka hægt að nota bytes.decode(read_ser)
      print(msg) 
      if(msg.strip()=="Hello From Arduino!"):
          blink(11)
    ```
   - Ef þú færð meldinguna `IndentationError: expected an indented block` þá þarftu að hreinsa til autt svæði(tab/enter) í python kóðanum


#### Bjargir

- [Raspberry Pi Arduino Serial Communication – Everything You Need To Know](https://roboticsbackend.com/raspberry-pi-arduino-serial-communication/)
- [pySerial documentation](https://pythonhosted.org/pyserial/)
- [Python 3 Unicode and Byte Strings](https://www.programiz.com/python-programming/methods/string/encode)


---

#### 3.3 Serial tenging, RPi til Arduino (2%)
Fylgdu tutorial: [Connect Your Raspberry Pi and Arduino Uno!](https://www.instructables.com/id/Connect-Your-Raspberry-Pi-and-Arduino-Uno/)
  
  - Skrifaðu og keyrðu Arduino kóðann í Arduino IDE í Raspberry Pi.
  - **Ath** Notaðu `str.encode()` til að breyta Unicode streng í bytes til að kóði virki.
  
---

#### 3.4 Bluetooth tenging, RPi til snjallsíma (2%)
Fylgdu tutorial: [Connect Your Raspberry Pi and Smartphone via bluetooth !](https://bluedot.readthedocs.io/en/latest/gettingstarted.html)
Munið að fylgja leiðbeiningum vel (ath lesa hverja síðu og fara í NEXT neðst á síðunni), ekki gleyma neinu!!!
  
  - Verkefnið er að rasberryPI prentar út "Hello World" þegar þið smellið á Blue Dot í síma ykkar (gera while true lúppu svo þið getið 
    smellt aftur og aftur.
  - [Blue Dot API](https://bluedot.readthedocs.io/en/latest/dotapi.html#module-bluedot)
  
---

#### 3.5 Bluetooth tenging, RPi til snjallsíma og LED (2%)
Fylgdu tutorial: [Bluetooth and BlueDot with LED !](https://bluedot.readthedocs.io/en/latest/recipes.html#flash-an-led)
  
  - Verkefnið er að rasberryPI kveikir á LED þegar smelt er á Blue Dot í snjallsíma :-) sem þýðir að þið verðið að tengja eina LED peru í breadboard
    og viðeigandi viðnám (reiknið) og tengja við RaspberryPi (ath gera while true lúppu svo þið getið 
    látið led blikka þegar smellt er á BlueDot). 
  -  Unnið er með [GPIOZero](https://www.raspberrypi.org/documentation/usage/gpio/python/) sem er þegar sett upp í RPi OS (default)
  
---

#### 3.6 Bluetooth tenging, RPi til snjallsíma og Myndavél (1%)
Fylgdu tutorial: [Bluetooth and BlueDot using remote camera !](https://bluedot.readthedocs.io/en/latest/recipes.html#remote-camera)
  
  - Verkefnið er að rasberryPI tekur mynd þegar smelt er á Blue Dot í snjallsíma :-) sem þýðir tenging við video :-)
  
---

#### 3.7 Bluetooth og Serial tenging (2%)

- Notaðu BlueDot með RaspberryPi til að kveikja á RGB LED peru sem er tengd við Arduino. 
- Það á að vera hægt að velja um 4 mismunandi liti með BlueDot.
- Getur þú látið BlueDot virka með fleiri litum?

---


#### 3.8 SPI Serial Peripheral Interface (SPI) (1%)
Kynntu þér Serial Peripheral Interface (SPI). Lestu [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol) og svaraðu eftirfarandi spurningum:
   
   1. Hvað er átt við með samstilltum (e. synchronous) samskiptastaðli?
   1. Hvað er master-slave samband, útskýrðu útfrá; MISO, MOSI, SCLK og CS/SS? 
   1. Hverjir eru helstu kostir og ókostir við SPI?
   
---

#### 3.9. (1%)
1. Fylgdu eftirfarandi tutorial: [Communication between two Arduino Boards](https://circuitdigest.com/microcontroller-projects/arduino-spi-communication-tutorial) og settu upp á Breadboard. **ATH.** notaðu þessa [rásarteikningu](https://raw.githubusercontent.com/VESM3/V21/master/Myndir/SPI.png) í staðinn fyrir þá sem er í greininni og þessa [kóða](https://gist.github.com/gestskoli/d2069beb5c4d0cf7c9351d75dfc3e2b0) í stað kóðanna sem eru í greininni. Sjá einnig [How do you use SPI on an Arduino?](https://arduino.stackexchange.com/questions/16348/how-do-you-use-spi-on-an-arduino). 


**SPI:**

- [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol)
- [SPI](https://www.allaboutcircuits.com/technical-articles/spi-serial-peripheral-interface/)
- [Arduino og SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all) 
- [SPI safnið fyrir Arduino](https://www.arduino.cc/en/reference/SPI)
- [Myndband um SPI](https://www.youtube.com/watch?v=ldRkXTBw9_o)

---

#### 3.10 Þráðlaus samskipti tveggja Arduino Uno með notkun nRF24L01. (3%)
  - Lestu vel og vandlega og fylgdu tutorial: [How nRF24L01+ Wireless Module Works & Interface with Arduino](https://lastminuteengineers.com/nrf24l01-arduino-wireless-communication/) 
  - **Ath** tengdu nRF24L01 við 3.3V output. Ekki tengja í 5V, það mun skemma nRF24L01
  - breyttu addressunni á rásinni (e. channel) fyrir samskiptin, notaðu háar tölur.
  - strengurinn inniheldur nafnið þitt (ekki Hello World)
  - Láttu LED lýsa hjá `transmitter` sem staðfestir að strengur hafi borist til `receiver`. 

---

#### 3.11 Samskipti í báðar áttir með Arduino Uno og nRF24L01. (3%)
- Tengdu tvo Arduino Uno með nRF24L01
- Sýndu samskipti sem fara í báðar áttir með tökkum og led perum.
- Sjá t.d. [NRF24L01 Tutorial](https://howtomechatronics.com/tutorials/arduino/arduino-wireless-communication-nrf24l01-tutorial/)

---

### Námsmat og skil

Gefið er heilt fyrir fullnægjandi lausn og svör, hálft ef ábótavant eða svör vanta.
Skilaðu á Innu vefslóð á **Github wiki** vefsíðu (**private**) sem inniheldur:

- Myndbönd af virkni úr verklegum tilraunum.
  - Passaðu að nafnið þitt og dagsetning komi fram (t.d. á miða) í öllum myndböndum.
- Kóði.
- Svör við spurningum

