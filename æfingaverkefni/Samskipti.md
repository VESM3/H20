### Samskipti 

Búðu til í **private** Github Repository vefsíðu (Verkefni 5) í Wiki sem inniheldur eftirfarandi:

- Svör við spurningum.
- Tengla á myndbönd af verklegum verkefnum (með nafn og dagsetningu á myndbandi).
- Tengla á kóðaskrár sem þú notar í verklegum verkefnum.

---

#### 1. SPI 
Lestu [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol) og svaraðu eftirfarandi spurningum:
   
   1. Hvað er átt við með samstilltum (e. synchronous) samskiptastaðli?
   1. Hvað er master-slave samband, útskýrðu útfrá; MISO, MOSI, SCLK og CS/SS? 
   1. Hverjir eru helstu kostir og ókostir við SPI?
   
---

#### 2. Serial Peripheral Interface (SPI)
1. Fylgdu eftirfarandi tutorial: [Communication between two Arduino Boards](https://circuitdigest.com/microcontroller-projects/arduino-spi-communication-tutorial) og settu upp á Breadboard. Sjá einnig [How do you use SPI on an Arduino?](https://arduino.stackexchange.com/questions/16348/how-do-you-use-spi-on-an-arduino)


**SPI:**

- [BASICS OF THE SPI COMMUNICATION PROTOCOL](https://www.circuitbasics.com/basics-of-the-spi-communication-protocol)
- [SPI](https://www.allaboutcircuits.com/technical-articles/spi-serial-peripheral-interface/)
- [Arduino og SPI](https://learn.sparkfun.com/tutorials/serial-peripheral-interface-spi/all) 
- [SPI safnið fyrir Arduino](https://www.arduino.cc/en/reference/SPI)


#### 3. Inter-Integrated Circuit (I2C) 
Lestu [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/) og svaraðu eftirfarandi spurningum:

   1. I2C notar message og address, hvað er það og hvernig virkar það?
   1. Hvað er hægt að senda mikið af gögnum (bits) í einu?
   1. Hver er helsti munurinn á SPI og I2C? 

---

#### 4. I2C með tvo Arduino 
Skoðaðu [I2C Communications](https://dronebotworkshop.com/i2c-arduino-arduino/) og settu upp síðari tilraunina **Remote Demo** (með breytiviðnámi og led) verklega (eða með TinkerCad).

Útskýrðu hvað eftirfarandi kóði gerir:

   1. `Wire.beginTransmission(ADDRESS);` Hvaða ADDRESS eru ekki í boði?
   1. `Wire.onReceive(receiveEvent);` og `Wire.onRequest(requestEvent);` 
   1. `Wire.requestFrom(SLAVE_ADDR, ANSWERSIZE);`

---



<!--

#### 5.2 UART 
Lestu [BASICS OF UART COMMUNICATION](https://www.circuitbasics.com/basics-uart-communication/) og svaraðu eftirfarandi spurningum:
 
   1. UART notast við baud rate útskýrðu nánar tilgang þess.
   1. Hvað er packet (START BIT, DATA FRAME, PARITY, STOP BITS) í UART?
   1. Hvernig er UART frábrugðið SPI? 
 
#### 5.1 UART
Kynntu þér UART [BASICS OF UART COMMUNICATION](https://www.circuitbasics.com/basics-uart-communication/) og [UART](https://www.allaboutcircuits.com/technical-articles/back-to-basics-the-universal-asynchronous-receiver-transmitter-uart/). Fylgdu eftirfarandi tutorial: [HOW TO SET UP UART COMMUNICATION ON THE ARDUINO](https://www.circuitbasics.com/how-to-set-up-uart-communication-for-arduino/) og settu upp á Breadboard.
   



-->
