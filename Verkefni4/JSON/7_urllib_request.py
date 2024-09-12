# urllib til að ná json skrár yfir netið
import urllib.request, json

# Fixing the SSL CERTIFICATE_VERIFY_FAILED Error
# https://realpython.com/urllib-request/#fixing-the-ssl-certificate_verify_failed-error  
# Lausn fyrir Mac notendur: Applications Folder -> Python folder, and click on the Install Certificates.command file

# JSON skrá hýst á Github sem Gist (max 60 request pr klst nema notað sé token). Vistaðu skránna með .JSON sniðmáti og veldu `raw` og afritaðu vefslóðina (url).
# Dæmi
with urllib.request.urlopen("https://gist.githubusercontent.com/GunnarThorunnarson/13839d272efae357adc1edbcd91f2938/raw/0175db90b92972daf7cf5142a986f28c9e923ae4/nemendur.json") as response:
    gogn = json.loads(response.read())
print(gogn)

# Prentum nafnið Þórður, gogn = dictionary 
print(gogn["nemendur"][0]["nafn"])
