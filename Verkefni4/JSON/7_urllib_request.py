# urllib til að ná json skrár yfir netið
import urllib.request, json

# JSON skrá hýst á Github (https) sem Gist (max 60 request pr klst nema notað sé token). Vistaðu skránna með .JSON sniðmáti og veldu `raw` og afritaðu vefslóðina (url).
with urllib.request.urlopen("https://gist.githubusercontent.com/GunnarThorunnarson/13839d272efae357adc1edbcd91f2938/raw/0175db90b92972daf7cf5142a986f28c9e923ae4/nemendur.json") as response:
    gogn = json.loads(response.read())
print(gogn)

# Prentum nafnið Þórður, gogn = dictionary 
print(gogn["nemendur"][0]["nafn"])
