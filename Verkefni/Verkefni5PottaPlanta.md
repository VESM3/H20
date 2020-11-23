## Verkefni 5: Pottaplanta (35%) 

Haust  2020 <br>
Einstaklingsverkefni.
Tími: 5 vikur.

---

### Verkefnalýsing:  Pottaplanta (sjálfgefið verkefni).

Verkefnið er í grunninn [þetta](https://learn.adafruit.com/pyportal-pet-planter-with-adafruit-io) (sleppum PyPortal og hátalara). Það sem bætist við er sjálfvirk vökvun og videocam sem tekur myndir af plöntu t.d samkvæmt tímaplani (adafruit IO) þannig er hægt að fylgjast með plöntu og líðan hennar :-) . Sjálvirk vökvun gæti t.d verið 2.lítra plastflaska opin að ofan svo hægt sé að fylla hana og plastslanga í tappa endanum sem fer í plöntupott, þar er [segulrofi](https://bc-robotics.com/tutorials/controlling-a-solenoid-valve-with-arduino/) sem opnar þegar vökva á plöntuna annars lokaður. Megnið af efni fáið þið í skóla, plastslöngur og segulrofa, að öllu leyti eru sömu kröfur á þetta verkefni og önnur. Það sem er kannski öðruvísi núna er að við viljum nota hærri spennu en venjulega þegar við notum segulrofa þá er það leyst með transistorum eða relay hér eru dæmi:

  * Rasberry Pi +12V [relay](https://www.iotdesignpro.com/projects/iot-based-solenoid-door-lock-using-raspberry-pi-4)
  * Arduino Uno +6V [Transistor](https://mechatrofice.com/arduino/solenoid-valve-control)
  

#### Verkþættir sem þarf að uppfylla:

- Unnið er með RaspberryPi og Arduino ef það á við.
- Unnið er með inntak frá skynjurum, tveimur eða fleirum (greint upplýsingar úr umhverfinu).
- Unnið með inntak til að stýra tengdum úttaksbúnaði.
- Gögn eru send frá inntaki með völdum samskiptaleiðum.
- Unnið er úr gögnum (forritun).
- Unnið er með vefviðmót eða smáforrit fyrir birtingu gagna og stýringar.
- Notkun vefþjónustu.
- Hanna IoT frumgerð (2D/3D hönnunarteikningar,rafrásarteikning).
- Samsettning á IoT búnaði (innfeld kerfi, vélbúnaður, tæki, skynjarar, íhlutir, brauðbretti, vírar osfrv.)
- Smíði IoT frumgerðar (veróborðsmíði, lóðun og samsettning) _með fyrirvara um að geta unnið í skólanum_.

---

### Verkefnaskil og skýrsla

Skilaðu hlekk á lokaða (e. private) Github geymslu á Innu sem inniheldur eftirfarandi:

- Allur kóði, skrár og gögn.
- Skýrsla (í readme.md) sem inniheldur:
  - verkefnalýsing ásamt hönnunarskissum.
  - rafrásarteikning.
  - hönnunarteikningar (til prentunar) 2d og eða 3d teikningar og model (.stl skráin).
  - tengil á myndband af notkun og virkni frumgerðar.
  - tengla á kóðaskrár.
  - ljósmyndir af samsettningu á IoT búnað og tilraunum. 
  - dagbók, hvað var gert og hvenær.
  - helstu hönnunarákvarðanir, heimildir og erfiðleikar og annað sem þér dettur í hug.
  - tengil á myndband af notkun og virkni IoT furmgerðar, með veróborðasmíð og hýsingu. (með fyrirvara).
  - ljósmynd af lóðun (báðar hliðar) af verosmíði. (með fyrirvara).
  
---

### Námsmat: Pottaplantan (sjálfgefið verkefni).

#### Grunnkröfur (60%):

1. Inntak, mælingar (skynjarar). **(10%)**
   - 10% Getur mælt hita og rakastig rétt.
   -  5% mæling ábótavant.
1. Gagnavinnsla og forritun með Adafruit IO og innfelld kerfi. **(10%)**
   - 10% Samantekt á meðaltal, há- og lággildi frá Soil sensor (raki og hiti i celsius) yfir tíma.
   -  5% Samantekt á hita í celsius og raka frá Soil sensor yfir tíma.
1. Viðmót. **(5%)**
   - 5% 
     - Viðmót í Adafruit IO sýnir nýjustu mælingar frá Soil sensor (hita og raka) og yfir tíma (línarit). 
     - Viðmót sýnir meðaltal, há- og lággildi.
   -  2.5% Viðmót sem sýnir mælingar frá Soil sensor (hita og raka) sem og samanburð yfir tíma (línarit).
1. Vefþjónusta (IFTTT) og Triggers. **(5%)**
   - 5% 
      - Notað er Scehdule Triggers til að taka mælingar reglulega með soil sensor. 
      - Notað er IFTTT vefþjónustu til að láta notanda vita að það þurfi að vökva plöntu.
   - 2.5% Vantar notkun með Scehdule Trigger eða IFTTT
1. Rafrásarhönnunarteikning. **(5%)**
   - 5% Hönnun er uppfyllt og framkvæmanleg og í samræmi við frumgerð eða verkefnalýsngu.
   - 2.5%  Hönnun er ábótavant og ekki alveg í samræmi við frumgerð.
   - 0%  Vantar eða stórlega ábótavant.
1. Hönnun IoT frumgerðar. **(15%)**
   - 15% 
     - Hönnun er góð, lögun umgjarðar fellur vel að frumgerð.
     - Allir íhlutir og skynjarar falla vel að hönnun.
     - Tengingar og samsettning er framkvæmanleg útfrá hönnun.
   - 10% Hönnun er uppfyllt að mestu leyti.
   -  5% Hönnun er gölluð eða ábótavant að nokkru leyti.
   -  0% Vantar eða stórlega gölluð.
1. Samsettning á IoT búnaði (tengja íhluti, viðnám, víra, brauðbretti osfrv.). **(10%)**
   - 10% Samsettning er í samræmi við rafrásarteikningu, lengd víra eru hóflegir og skipulagðir.
   - 5% Ábótavant.
    
#### Aukakröfur:
1. Camera **(20%)**
   - 20% 
      - Myndir eru teknar með notkun Scehdule Triggers. 
      - Myndir sýna vöxt plöntu yfir tíma í viðmóti (allar teknar myndir), sent yfir netið.
      - Samsettning og hönnun er til fyrirmyndar.     
   - 15% 
      - Myndir eru teknar með notkun Scehdule Triggers. 
      - Nýjasta myndin birtist í AdafruitIO.
      - Samsettning og hönnun er til fyrirmyndar.  
   - 10%
      - Myndir eru teknar með RPi.
      - Myndir eru sendar til notanda.
      - Samsettning og hönnun er til fyrirmyndar.  
   -  5% Myndavél tekur mynd af plöntu og eru vistaðar.
1. Vökvakerfi **(20%)**
   - 20% 
      - Notað er Reactive trigger til að stýra vökvun þegar þess er þörf. 
      - Notandi getur stillt magn vökva fyrir vökvun í Adafruit IO viðmóti.
      - Notað er IFTTT til að tilkynna um vökvun til notanda.
      - Samsettning og hönnun er til fyrirmyndar.
   - 15% 
      - Notað er Reactive Trigger til að stýra vökvun. 
      - Notað er IFTTT til að tilkynna um vökvun til notanda. 
      - Samsettning og hönnun er til fyrirmyndar.
   - 10%
      - Notað er Schedule Trigger en ekki Reactive Trigger til að stýra vökvun. 
      - Notað er IFTTT til að tilkynna um vökvun til notanda. 
      - Samsettning og hönnun er til fyrirmyndar.
   -  5% Vökvun virkar með segulloku. 
1. Smíði IoT frumgerðar og samsettning eftir prentun **(15%)**
   - 15% 
      - Samsettning er í samræmi við prentun. 
      - Tengingar eru í samræmi við rafrásarteikningu og vel útfærðar.
      - Veróborðsmíð er til fyrirmyndar.
      - Lóðun og lengd víra eru hóflegir og skipulagðir.
   - 10% Samsettning, tengingar, lóðun eða veróborð útfærsla er ábótavant.
   -  5% Samsettning, tengingar, lóðun, veróborð er óklárað eða stórlega ábótavant.


<!-- 

vatnshæðamælir. í vatnstank.
ljósnemi til að halda utan um birtustig.
ljósperu til ræktunar.
áburður og motorar.

-->

