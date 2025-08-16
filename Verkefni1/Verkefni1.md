## Verkefni 1 
10% af heildareinkunn

---

Útfærðu einfaldan vef með [Flask](https://flask.palletsprojects.com/en/2.3.x/) og einföldu [Jinja](https://jinja.palletsprojects.com/en/3.0.x/templates/) template (ekki nota _include_ eða _inheritance_ í þessu verkefni). Vefurinn inniheldur tvær vefsíður, forsíðu og aukasíðu. Innihald vefsíðunnar skal vera áhugamál.  Notaðu VSCode ritilinn og settu upp FLASK í **VENV** umhverfi.

1. Forsíðan inniheldur valmynd ( sjá lið 4 ) og ljósmynd [static skrá](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/staticFiles.py) sem tengist áhugamálinu **(35%)**
1. Auka síðan inniheldur valmynd ( sjá lið 4 ) og helstu upplýsingar um þitt áhugamál í röðuðum lista (`ol`). Þessi gögn eru geymd í `dictionary` í app.py skrá. **(35%)**
1. Notaðu eigið CSS safnið fyrir útlit og uppsetningu **(10%)**
1. Vefur skal innihalda lárétta valmynd með tveimur hlekkjum . Notaðu [static route](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/staticRoutes.py) fyrir síðurnar og [url_for](https://github.com/vefthroun/Vefforritun1/blob/main/Verkefni1/namsefni/urlfor.py) fyrir hlekkina í valmynd. **(20%)**

#### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna. Innihald (gögn) eiga aldrei að vera skrifuð beint í html!
  
---

### Námsmat og skil
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (_ekki venv möppu_) á Innu.
