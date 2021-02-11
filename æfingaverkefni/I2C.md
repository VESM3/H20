
## Inter-Integrated Circuit (I2C) 

#### Inter-Integrated Circuit (I2C) 
Lestu [I2C](https://www.circuitbasics.com/basics-of-the-i2c-communication-protocol/) og svaraðu eftirfarandi spurningum:

   1. I2C notar message og address, hvað er það og hvernig virkar það?
   1. Hvað er hægt að senda mikið af gögnum (bits) í einu?
   1. Hver er helsti munurinn á SPI og I2C? 

---

#### I2C með tvo Arduino 
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
