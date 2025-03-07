## Verkefni 1 
10% af heildareinkunn

---

Útfærðu einfaldan vef með [Flask](https://flask.palletsprojects.com/en/2.3.x/) og einföldu [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/) template (ekki nota _include_ eða _inheritance_ í þessu verkefni). Vefurinn inniheldur tvær vefsíður auk 404 error vefsíðu (error_route). Innihald vefsíðunnar skal vera áhugamál.  Notaðu VSCode ritilinn og settu upp FLASK í **VENV** umhverfi.

1. Láréttur menu á vefsíðu sem inniheldur tvo hlekki. Notaðu [static route](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/staticRoutes.py) fyrir síðurnar og [url_for](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/urlfor.py) fyrir hlekkina í menu. **(20%)**
1. Forsíðan inniheldur menu og ljósmynd [static skrá](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/staticFiles.py) sem tengist áhugamálinu **(10%)**
1. Hin síðan inniheldur menu og helstu upplýsingar um þitt áhugamál í óröðuðum lista (`ul`). Þessi gögn eru geymd í `dictionary` í app.py skrá. **(30%)**
1. [404 Error](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/errorHandlingStatusCodes.py) vefsíða sýnir textaskilaboð (frá breytu) og einhverja skemmtilega 404 mynd [static skrá](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/staticFiles.py) **(20%)**
1. Notaðu [New CSS](https://newcss.net/) CSS safnið fyrir útlit og uppsetningu **(20%)**


#### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna. Innihald (gögn) eiga aldrei að vera skrifuð beint í html!
  
---

### Námsmat og skil
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (_ekki venv möppu_) á Innu.
