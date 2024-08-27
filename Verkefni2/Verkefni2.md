## Verkefni 2 
- 15% af heildareinkunn
- Viðfangsefni: 
   1. Listi með dictionaries
   1. Dynamic routing 
   1. Jinja2: include og if-statement
   1. Pico CSS safnið

---

### Verkefnalýsing 
Útfærðu [blog](https://www.visindavefur.is/svar.php?id=3225) með Flask. Búðu til 10 blogfærslur að eigin vali, notaðu t.d. ChatGPT til að búa til gögnin. Notaðu lista með dictionaries (blogfærslur) sem gagnagrind (datastructure), hér er [sýnidæmi](#data) með blogfærslur.

1. Vefurinn er hlutaður niður með **include** í Jinja2; nav (valmynd), footer (höfundur verkefnis) og blogfærslu. **10%**
1. Valmynd inniheldur hlekki á forsíðu og **3** flokka úr gagnagrind. Sýndu hvaða hlekkur er virkur hverju sinni [sýnidæmi](https://python-web.teclado.com/section12/lectures/03_base_template_and_nav_bar/#highlighting-the-currently-active-page). **10%**
1. Forsíða inniheldur html töflu, yfirlit yfir allar blogfærslur; höfundur, titill, flokkur, dagsetning og hlekk (hnapp) á blogfærslu. Sýndu einnig heildarfjölda blogfærslna. **20%**
1. Blogfærsla (undirsíða) inniheldur; titil, málsgrein (textainnihald), mynd, höfund og dagsetningu. Notaðu `div` til að halda utan um blogfærslu. **20%**
1. Flokkur (undirsíða). Ef notandi velur t.d. hlekkinn **Flask** úr valmynd þá birtist vefsíða einungis með blogfærslum úr þeim flokki. **20%**
1. Notaðu [Pico]([https://purecss.io/](https://picocss.com/)) safnið fyrir uppsetningu og framsetningu á vef. **20%**

Engin harðkóðun!

#### data

```python
# Dæmi um blogfærslu (dictionary) í lista.
blog_posts =  [
        {
            "id": 0,
            "title": "Hvað er Jinja2",
            "content": "Jinja2 er templatekerfi ...",
            "picture": "mynd0.JPG",
            "author": "Gunnar",
            "category": "Jinja2",
            "date_posted": "20.08.2024"
        },
        {
            "id": 1,
            "title": "Hvað er Pico",
            "content": "Pico er CSS safn ...",
            "picture": "mynd1.JPG",
            "author": "Karl",
            "category": "CSS",
            "date_posted": "21.08.2024"
        },
        {
            "id": 3,
            "title": "Hvað er Flask",
            "content": "Flask er microframework ...",
            "picture": "mynd2.JPG",
            "author": "John Doe",
            "category": "Flask",
            "date_posted": "23.08.2024"
        }    
]

```

**Punktar**
-  Notaðu `id` úr gagnagrind fyrir url í dynamic route
-  dæmi um hlekk með _url_for_ `<a href="{{ url_for('flokkur', fl='Flask') }}" ` á dýnamískt route  `@app.route('/flokkur/<fl>')`
-  Þú gætir þurft að breyta streng í heiltölu t.d. id = int("3")  # breytum "3" í 3 með int()

---

### Námsmat og skil 
Gefið er fullt fyrir hvern lið sem er fullnægjandi, hálft ef hann er að hluta til kominn og ekkert ef hann vantar. Skilaðu möppu með öllum skrám (ekki venv möppu) á Innu.

