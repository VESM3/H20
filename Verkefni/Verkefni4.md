### Verkefni 4 (20%) _drög_

Einstaklingsverkefni <br>
Tími: 3 vikur

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

#### 4.1 Digital Input (2%)
Sendu stöðu hnapps á/af (í rauntíma ) sem er tengdur við Raspberry Pi til Adafruit IO. Skoðaðu niðurstöður með _Gauge block_ í Dashboard.
Skoðaðu Adafruit IO Basics tutorial: [Digital Input](https://learn.adafruit.com/adafruit-io-basics-digital-input) með notkun RaspberryPi (ekki Arduino). 

- Þú þarft ekki að nota `T-Cobbler Plus - GPIO Breakout`
- Þú þarft ekki að nota `adafruit_blinka` safnið, notaðu frekar t.d. RPi.GPIO safnið.

---

#### 4.2 Digital Output (2%)
How to turn a LED on and off from Adafruit IO using any modern web browser.<br>
Skoðaðu Adafruit IO Basics tutorial: [Digital Output](https://learn.adafruit.com/adafruit-io-basics-digital-output) með notkun RaspberryPi (ekki Arduino).

- Þú þarft ekki að nota `T-Cobbler Plus - GPIO Breakout`
- Þú þarft ekki að nota `adafruit_blinka` safnið, notaðu frekar t.d. RPi.GPIO safnið.

---

#### 4.3 Circuit Triggers Internet Action. (3%)
Notaðu takka á brauðbretti sem er tengt við RaspberryPi sem sendir skilaboð til Adafruit IO þegar ýtt er á hann. Notaðu `RPi.GPIO` safnið fyrir GPIO (ekki `adafruit_blinka`).

Notaðu einnig vefþjónustu að eigin vali (t.d email, sms, twitter osfrv.) hjá [IFTTT (If This Then That)](https://ifttt.com/) sem vaktar þetta `feed` hjá Adafruit IO og lætu þig vita þegar smellt er á takkann. 

Sjá [IFTTT uppsetningu](https://learn.adafruit.com/using-ifttt-with-adafruit-io/ifttt-to-adafruit-io-setup) <br>
_Create -> if This -> Adafruit -> Any new data -> Veldu viðeigandi feed -> Create Trigger -> Then That og veldu vefþjónustu að eigin vali_

> A basic project that triggers an internet action when a physical switch is activated.
> The code will detect the switch and send a message to a feed on the cloud data site Adafruit IO. Another cloud services site, IFTTT, will 
> monitor this feed and send an email when activity is detected 

---

### Fleiri verkefni væntanleg!

---

### Námsmat og skil

Gefið er fullt fyrir fullnægjandi lausn, hálft ef ábótavant.
Skilaðu á Innu vefslóð á Github wiki vefsíðu (**private**) sem inniheldur:

- Kóða (taktu út KEY upplýsingar)
- Myndbönd af virkni úr verklegum tilraunum. 
- Passaðu að nafnið þitt og dagsetning komi fram (t.d. á miða) í öllum myndböndum.

