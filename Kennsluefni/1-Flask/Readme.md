### Hvað er Flask
[Flask](https://flask.palletsprojects.com/en/2.3.x/) er Python veframmi (_web framework_) sem er byggður á litlum kjarna og auðvelt er að framlengja hann með viðbótum í pakkaformi (_package manager_). Flask er talið meira _Pythonic_ en Django veframminn vegna þess að Flask vefforrit er skýrara (_explicit_). 

---

### Uppsetning á Flask með VENV 
[Flask tutorial in VS Code](https://code.visualstudio.com/docs/python/tutorial-flask).

_[Lausnir]((Vandamal.md)) á hugsanlegum vandamálum við uppsetningu á VENV eða Flask_

---

### Halló heimur
1. Búðu til [app.py](Routes/halloheimur.md) skránna í Visual Studio Code Editor 
1. vistaðu `app.py` í möppu sem inniheldur einnig venv möppuna   (aldrei nefna skrá "flask.py")
1. Keyrðu python skránna: notaðu play takkann í VSCode eða skrifað í terminal: `flask run` eða `python app.py`
1. Skoðaðu vefsíðuna í vafra

---

### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna.


<!--
#### Uppsetning vefþróunarsvæðis, leiðbeiningar <br>(Windows með Command Promt, CMD. Mac með Terminal)

1. Þú þarft að hafa nýlega stöðuga (stable) útgáfu af python þýðanda.
    1. Til að kanna núverandi útgáfu:  `python --version`  (td. powershell í pc)
1. Vefþróunarsvæði (_virtual environment_)
    1. búðu til möppu t.d. _vefforitun_ í tölvunni t.d. á C: rót: `mkdir vefforritun`
    1. færðu þig í nýju möppuna `cd vefforritun`
    1. settu upp vefþróunarsvæði (virtual environment): (pc) `py -3 -m venv .venv`  (mac) `python3 -m venv .venv` 
    1. Virkjaðu svæðið (activate venv):  (pc) `.venv\Scripts\activate` (mac) `. .venv/bin/activate`
1. Insetning Flask (Install flask framework)
    1. Activate venv: `.venv\Scripts\activate`
    1. Notaðu pip til að setja inn (install) flask: `pip install flask`
    1. Opnaðu python þýðandann: `python` (í VCS _terminal_)           
    1. Athugaðu hvort flask sé virkt (active):  `>>> import flask`  
    1. ef það er engin villumelding þá tókst það.  `>>> quit()`
1. Halló heimur
    1. Búðu til [app.py](Routes/halloheimur.md) skránna í Visual Studio Code Editor 
    1. Ekki nefna skrá "flask.py" nema að þú viljir lenda í vandræðum  
    1. vistaðu `app.py` í _vefforitun_ möppunni sem geymir einnig venv möppuna
1. Að keyra og sjá app.py á innbyggðum local server
    1. Keyrðu python skránna: `flask run` eða `python app.py`
    1. Skoðaðu vefsíðuna í vafra

-->

<!--

### VS Code ritill
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Activate Environments in Terminal Using Environment Variables](https://github.com/microsoft/vscode-python/wiki/Activate-Environments-in-Terminal-Using-Environment-Variables)
  
#### VSCode og VENV
1. Náðu þér í python stuðning sem er viðbót (extension) í VS Code [Python linting](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. Opnaðu möppuna sem geymir python skrárnar fyrir flask appið.
1. Veldu python þýðandann sem er í venv (neðst í VSCode) prófað að keyra (Play takkinn) python skrá með `Code runner` extension í VSCode.
1. (venv) er virkt (_activate_) sjálfkrafa þegar við opnum terminal innan VS Code  


#### Aðrar gagnlegar stillingar í VSCode
1. Debugger. Hægt er að búa til og stilla `launch.json` config (taka t.d. út no-reload í "args") 
1. Git og Github. Það er nauðsynlegt er að búa til `.gitignore` skrá  til að hunsa `venv` möppu og `.vscode skrá, við vijum ekki hafa þetta með í git aðgerðum. Hægt er að tengja Git við Github repository í VSCode.
-->

<!--
1. .vscode -> settings.json  sýnir hvaða þýðandi verið að nota fyrir project.
1. Til að sækja söfn t.d. flask þá notum við [pip (python package installer)](https://pypi.org/) `pip install flask` 
1. Við getum skoðað hvaða viðbætur við höfum sett í `env/Lib/site-packages/` þessar viðbætur tilheyra eingöngu vefþróunarsvæðinu 

- Video: [First install and Virtual Environments - Windows 10](https://www.youtube.com/watch?v=x1cbYa2SSlE)
- Video: [Visual Studio Code (Windows) - Setting up a Python Development Environment - Corey Shafer](https://www.youtube.com/watch?v=-nh9rCzPJ20)
- Video: [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
-->
 



