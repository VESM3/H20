# Verkefni 5: Pottaplanta (35%) 
- Einstaklingsverkefni <br>
- Vor 2021 <br>

---

### Verkefnalýsing:  Pottaplanta.

Verkefnið er í grunninn að sinna pottaplöntu með notkun skynjara fyrir mælingar og IoT til að fylgjast með líðan hennar. Við notum [jarðvegsmælir (e. soil sensor)](https://github.com/VESM3/H20/blob/master/Gogn/soilsensor.md) til að kanna rakastig jarðveg og [hitaskynjara](https://randomnerdtutorials.com/9-arduino-compatible-temperature-sensors-for-your-electronics-projects/) fyrir hitastig svo við getum áttað okkur hvenær við þurfum að vökva plöntuna. Með ljósnema (t.d. [LDR](https://create.arduino.cc/projecthub/tarantula3/using-an-ldr-sensor-with-arduino-807b1c)) könnum við einnig birtuþörf plöntunar og kveikjum á gróðurlampa (led pera) eftir þörfum. Sjá sýnidæmi [myndband](https://www.youtube.com/watch?v=YXDoPfLlGHs&feature=youtu.be). 

---

### Verkþættir sem þarf að uppfylla:

1. Unnið er með skynjara (raki í jarðvegi, hitasstig og ljósnema) til að greina upplýsingar úr umhverfinu.
1. Gögn eru send frá inntaki (Arduino) með völdum samskiptaleiðum (t.d. serial tenging) til Raspberry PI.
1. RaspberryPi sér um að senda og taka við upplýsingum yfir netið til Adafruit IO platform.
1. Stýringar. Unnið með Triggers frá Adafruit IO til að stýra tengdum úttaksbúnaði (kveikja á LED)
1. Unnið er með vefviðmót fyrir birtingu gagna (Dashboard í Adafruit IO).
1. Notað er vefþjónusta (IFTTT) til að láta vita hvenær þörf er á að vökva plöntu (t.d. email)
1. Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.) er með besta móti.

---

## Námsmat

### Grunnkröfur, án notkuna Adafruit IO. (50%)

1. Inntak (mælingar). 
   - 20% Getur mælt birtu, hita og jarðvegsrakastig.
   - 10% Getur mælt jarðvegsrakastig og hitastig en birtustig vantar eða er ábótvant.
   -  5% tvær eða fleiri mælingar vantar eða eru ábótavant.
1. Viðmót. 
   - 15% jarðvegsrakamælingar og hitastig (celsius) eru birtar í [16x2 LCD](https://lastminuteengineers.com/arduino-1602-character-lcd-tutorial/) skjá með Arduino, sjá t.d. [DHT11 SENSOR](https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-an-arduino/) og [Temperature & Humidity to RPi](https://www.instructables.com/Sending-Temperature-Humidity-Data-From-Arduino-to-/)
   - 10% jarðvegsrakaupplýsingar eru birtar í 16x2 LCD skjá með Arduino.
   -  5% Upplýsingar birtast eingöngu í serial monitor með Arduino.
1. Stýringar.
   - 15% 
     - Kveikt er á LED peru úrfrá ljósmælingu (LDR skynjari) ef það verður skyndilegt myrkur.
     - Kveikt er á led peru yfir ákveðið tímabil (daginn) annars er slökkt.
   - 10% Kveikt er á led peru yfir ákveðið tímabil (daginn) og slökkt á öðrum tíma (nótt).
   - 5% Stýring er ábótavant.

### IoT viðbót, með notkun Adafruit IO. (50%)
1. Viðmót í Adafruit IO. Sjá sýnidæmi [Pet Planter with Adafruit IO](https://learn.adafruit.com/pyportal-pet-planter-with-adafruit-io/adafruit-io-setup)
   - 20%
      - Viðmót sýnir nýjustu mælingar; hita í celsíus, jarðvegsraka og birtustig.
      - Viðmót sýnir þróunina hita og jarðvegsraka yfir tíma (línurit). 
     <!--  - Viðmót sýnir meðaltal, há- og lággildi.  -->
   - 15%
      - Viðmót sýnir nýjustu mælingar; jarðvegsrakastig, en það vantar hita- eða birtustig.
      - Viðmót sýnir þróunina hita og jarðvegsraka yfir tíma (línurit). 
   - 10%
      - Viðmót sýnir nýjustu mælingar á jarðsvegsrakastig sem og samanburð yfir tíma (línarit).
   -  5%
      - Viðmót er ábótavant, sýnir takmarkaðar eða rangar upplýsingar.
1. Vefþjónusta (IFTTT)  
   - 10%  Notað er IFTTT vefþjónustu til að láta notanda vita að það þarf að vökva plöntu útfrá upplýsingum frá rakaskynjara.
   -  5%  Virkni er ábótavant.
1. Stýringar 
   - 20% 
      - Notað er Reactive trigger til að kveikja á led peru útfrá upplýsingum frá ljósnema (myrkur).
      - Notað er Schedule Trigger til að kveikja og slökkva á led peru yfir ákv. tímabili (dagur/nótt).
   - 10% 
      - Notað er Schedule Trigger til að kveikja á led peru yfir ákv. tímabili (dagur/nótt).
      
---

## Verkefnaskil og skýrsla

Skilaðu hlekk á lokaða (e. private) Github geymslu á Innu sem inniheldur eftirfarandi:

1. Allur kóði, skrár og gögn.
1. Skýrsla (í readme.md) sem inniheldur:
   1. dagbók, hvað var gert og hvenær.
   1. ljósmyndir af samsettningu á IoT búnað og tilraunum. 
   1. tengil á kóðaskrár og myndband af notkun og virkni frumgerðar (án notkunar Adafruit IO)
   1. tengil á kóðaskrár og myndband af notkun og virkni IoT furmgerðar (með notkun Adafruit IO)
  
