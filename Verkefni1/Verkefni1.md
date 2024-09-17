## Verkefni 1 
10% af heildareinkunn

---

Útfærðu einfaldan vef með [Flask](https://github.com/vefthroun/Vefforritun1/tree/main/Kennsluefni/1-Flask#hva%C3%B0-er-flask) og einföldu [Jinja](https://github.com/vefthroun/Vefforritun1/tree/main/Kennsluefni/1-Flask/Templates) template (ekki nota _include_ eða _inheritance_ í þessu verkefni). Vefurinn inniheldur forsíðu, _Um mig_ síðu og 404 error sérútfærða vefsíðu. Notaðu VSCode ritilinn og settu upp FLASK í **VENV** umhverfi. 

1. Láréttur menu á _forsíðu_ og _Um mig_ síðu inniheldur tvo hlekki. Notaðu [static route](https://github.com/vefthroun/Vefforritun1/blob/main/Kennsluefni/1-Flask/Routes/1_staticRoutes.py) fyrir síðurnar og [url_for](https://github.com/vefthroun/Vefforritun1/blob/main/Kennsluefni/1-Flask/Routes/8_urlfor.py) fyrir hlekkina í menu. **(20%)**
1. Forsíðan inniheldur menu og random ljósmynd ([https://picsum.photos/](https://picsum.photos/) ) **(10%)**
1. _Um mig_ síðan inniheldur menu og persónuupplýsingar. Birtu nafn, aldur og netfang í óröðuðum lista (`ul`) og smá um þig t.d. áhugamál í málsgrein (`p`) í HTML. Þessi gögn eru geymd í `dictionary` í app.py skrá. **(30%)**
1. [404 Error](https://github.com/vefthroun/Vefforritun1/blob/main/Kennsluefni/1-Flask/Routes/5_errorHandlingStatusCodes.py) vefsíða sýnir textaskilaboð (frá breytu) og einhverja skemmtilega 404 mynd ([static skrá](https://github.com/vefthroun/Vefforritun1/blob/main/Kennsluefni/1-Flask/Routes/7_staticFiles.py)) **(20%)**
1. Notaðu [New CSS](https://newcss.net/) CSS safnið fyrir útlit og uppsetningu **(20%)**


#### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna. Innihald (gögn) eiga aldrei að vera skrifuð beint í html!
  
---

### Námsmat og skil
- Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar.
- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (_ekki venv möppu_) á Innu.
