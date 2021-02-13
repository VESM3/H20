### Verkefni 4 (20%) 

Einstaklingsverkefni <br>

---

#### Adafruit IO umhverfið 
1. AdafruitIO+ aðgangur
   - Náðu í Adarfuit IO+ aðgang (1 ár frítt) hjá [Github Student Pack](https://education.github.com/pack) og tengdu saman Github og [Adafruit](https://www.adafruit.com/) reikning.
   - Í Adafruit reikningnum skaltu velja `services`, `view discount` (þar er kóðaruna fyrir Adafruit IO).
   - Skráðu þig inn hjá [Adafruit IO](https://io.adafruit.com/). Veldu `Upgrade to IO+` og smelltu svo á hnappinn `Redeem a Coupon or Pass` og settu inn rununa til að fá 1 ár frítt. Ath. það þarf aldrei að gefa upp kredikortaupplýsingar.
1. Skoðaðu vel [Welcome to Adafruit IO](https://learn.adafruit.com/welcome-to-adafruit-io/overview) og [Adafruit IO (myndbönd)](https://learn.adafruit.com/all-the-internet-of-things-episode-four-adafruit-io/how-adafruit-io-works)
1. Kynntu þér hvernig [Feeds](https://learn.adafruit.com/adafruit-io-basics-feeds) og [Dashboards](https://learn.adafruit.com/adafruit-io-basics-dashboards) virka.

**Bjargir:**

- [Adafruit IO Python](https://adafruit-io-python-client.readthedocs.io/en/latest/quickstart.html) safn til að tengjast og nota RPi með Adafruit IO (MQTT og HTTP)
- [Python kóði með tutorials](https://github.com/adafruit/Adafruit_IO_Python/tree/master/examples/basics).
- AdafruitIO [forum](https://forums.adafruit.com/viewforum.php?f=56) og [discord](https://discord.com/invite/adafruit)
- "halló heimur" myndband: [Connecting the Raspberry Pi to Adafruit IO cloud](https://www.youtube.com/watch?v=IfzpoFGkmns)

---

#### 4.1 Digital Input (3%)
1. Sendu stöðu hnapps á/af (í rauntíma) sem er tengdur við Raspberry Pi til Adafruit IO. 
1. Skoðaðu niðurstöður með **Gauge block** í Dashboard. 

Sjá [Digital Input (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-input). 
Notaðu **RPi.GPIO** safnið í staðinn fyrir `adafruit_blinka`. Þú þarft ekki að nota `T-Cobbler Plus - GPIO Breakout`

---

#### 4.2 Digital Output (3%)
1. Tengdu eina LED í brauðbretti með viðnámi tengt við RaspberryPi.
1. Kveiktu og slökktu á LED með **toogle** hnapp í Dashboard í Adafruit IO. 

Sjá [Digital Output (Python)](https://learn.adafruit.com/adafruit-io-basics-digital-output). Notaðu **RPi.GPIO** safnið í staðinn fyrir `adafruit_blinka`.

---

#### 4.3 Schedule Triggers (MQTT)  (3%) 

1. Tengdu eina led peru í brauðbretti með viðnámi tengt við RaspberryPi.
1. Notaðu [Schedule Triggers (python)](https://learn.adafruit.com/adafruit-io-basics-scheduled-triggers) til að kveikja og slökkva á led með reglulegu mínútu millibili.

**ath.** Í þessu dæmi notum við aðeins einn RaspberryPi. Eðlilegra væri að vinna með tvo eða fleiri endapunkta (t.d. 2 x arduino) sem er nettengdir.

---

#### 4.4 Reactive Triggers (3%) 
Skoðaðu [How to Use Triggers in Your Adafruit IO Project](https://www.digikey.com/en/maker/blogs/2019/how-to-use-triggers-in-your-adafruit-io-project)

1. Tengdu [Ljósviðnám](https://learn.adafruit.com/basic-resistor-sensor-reading-on-raspberry-pi/basic-photocell-reading) og led peru í brauðbretti með viðnámi tengt við RaspberryPi.
1. búðu til `reactive trigger` í Adafruit IO sem lætur led peru kveikja á sér þegar það dimmir en slekkur á sér þegar það er bjart.

**ath.** Í þessu dæmi notum við aðeins einn RaspberryPi. Eðlilegra væri að vinna með tvo eða fleiri endapunkta (t.d. 2 x arduino) sem er nettengdir.

---

#### 4.5 Services. Circuit Triggers Internet Action. (2%)
1. Notaðu takka á brauðbretti sem er tengt við RaspberryPi sem sendir skilaboð til Adafruit IO þegar ýtt er á hann. Notaðu `RPi.GPIO` safnið fyrir GPIO (ekki `adafruit_blinka`).
1. Notaðu [IFTTT (If This Then That)](https://ifttt.com/) skýþjónustu sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita með `email` þegar smellt er á takkann. Sjá [IFTTT uppsetningu](https://learn.adafruit.com/using-ifttt-with-adafruit-io/ifttt-to-adafruit-io-setup) <br>
_Create -> if This -> Adafruit -> Any new data -> Veldu viðeigandi feed -> Create Trigger -> Then That og veldu vefþjónustu_<br>
IFTTT hefur allskonar vefþjónustur sem þú getur nýtt þér, skoðaðu hvað er í boði.

---

#### 4.6 Analog Output (3%)

Notaðu **Slider block** `(min value 0, max vale 1024)` í **Dashbord** með Adafruit IO til að stýra birtustig á LED sem er tengd við PWM pinna á RaspberryPi. <br>

Sjá eftirfarandi til viðmiðunar:
- [Kóðalausn, en með notkun PWM driver (erum ekki með)](https://learn.adafruit.com/adafruit-io-basics-analog-output/python-code)
- [RPi Python Programming 16: Analog output and software PWM](https://www.engineersgarage.com/raspberrypi/articles-raspberry-pi-python-software-pwm-led-fading/)
- [Raspberry Pi PWM Tutorial | Control Brightness of LED](https://electronicshobbyists.com/raspberry-pi-pwm-tutorial-control-brightness-of-led-and-servo-motor/)

---

#### 4.7 Analog Input með Arduino (3%)
1. Tengdu ljósviðnám í brauðbretti tengt við Arduino.
1. Sendu mælingar (analog gildi) frá ljósviðnámi (e. photocell) til RaspberryPi 
1. RaspberyPi sendir áfram gildin til Adafruit IO. 
1. Birtu rauntímaniðurstöður með _Gauge block_ og línuriti í Dashboard.

Sjá til viðmiðunar:
- [Analog Input (Arduino)](https://learn.adafruit.com/adafruit-io-basics-analog-input) 
- [python kóði með notkun MCPP3008 ADC converter](https://github.com/adafruit/Adafruit_IO_Python/blob/master/examples/basics/analog_in.py) 

---

### Námsmat og skil

Gefið er fullt fyrir fullnægjandi lausn, hálft ef ábótavant.
Skilaðu á Innu vefslóð á Github wiki vefsíðu (**private**) sem inniheldur:

- Kóða (taktu út KEY upplýsingar)
- Myndbönd af virkni úr verklegum tilraunum. 
- Passaðu að nafnið þitt og dagsetning komi fram (t.d. á miða) í öllum myndböndum.

