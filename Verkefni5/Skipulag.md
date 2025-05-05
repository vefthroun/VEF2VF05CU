# Verkáætlun

### Tímáætlun

| Vika | Tími 1  | Tími 2 | Tími 3 | Tími 4 | 
| --- | --- | --- | --- | --- | 
| 19 | Gagnaöflun og skipulag | Forritun | Forritun | Forritun | 
| 20 | Forritun | Forritun | Uppsetning | Frágangur og skil |

### Vika 19

1. Gagnaöflun
   * Jason gagnagrunnur
   * Skipurit 
   * Texti og myndir
2. Forritun - uppsetning 
3. Json API tenging
4. Forritun - Admin

### Vika 20

1. Forritun - CRUD
2. Forritun 
3. Uppsetning á Internetið
4. Frágangur

---

### Verkefnaskil

* **Föstudagur 16. maí. Kl. 23:59**
* Verkefni 5 er _lykilmatsþáttur_. 

> Athugið að ef verkefninu hefur ekki verið skilað fyrir **kl. 8 á mánudagsmorgun 19. maí** (_Deadline_) þá er ekki hægt að fara yfir verkefnið og viðkomandi er _fallinn_ í áfanganum.

---

### Undirbúningsvinna

Gerið grein fyrir skipulagi og virkni vefsins

#### Efnisyfirlit - _Site map_

_Dæmi miðað við grunnkröfur:_

1. app innihald (__init__)
   * blog.py
   * admin.py
2. blog.py 
   * header, efnisyfirlit með flokkavali
   * main, birtir gögn úr Json skrá
   * aside, sækir gögn úr Json API
3. admin.py
   * header, efnisyfirlit
   * aðgangi lokað með session
   * stjórnborð (_dashboard_)
     * yfirlit yfir allar pósta í töflu. Hægt er að breyta eða eyða póstum
     * síða þar sem hægt er skrifa nýjan póst
     * síða þar sem hægt er að breyta póstum

#### Json gagnagrind

1. tinydb (_default) 
   1. id
   2. flokkur
   3. postur
   4. dagsetning
   5. .....

#### Nýungar

Gerið grein fyrir eigin hönnun og forritun sem ekki er tiltekin í grunnkröfum verkefnisins.

Dæmi:

* Vefurinn verður hýstur á [Pythonanywhere.com](https://www.pythonanywhere.com/)