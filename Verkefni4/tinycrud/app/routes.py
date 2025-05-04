from app import app

from tinydb import TinyDB
db = TinyDB('data/db.json', indent = 2, encoding='utf-8', ensure_ascii=False)

@app.route('/')
def index():
    return "<a href='/read'>Lesa</a> | <a href='/create'>Skrifa</a> | <a href='/update'>Uppfæra</a> | <a href='/delete'>Eyða</a>"

@app.route('/read')
def read():
    for i in db:
        print(i)
    return "Allir í db - skoðið terminal"

@app.route('/create')
def create():
    plus1 = len(db) +1
    print(plus1)
    db.insert({
            "uid":plus1,
            "name":"Jóhannes",
            "email":"joh@nn.es",
            "bio":"Skírn er mín sérgrein"})
    for i in db:
        print(i)
    return "Nýr notandi er í db.json - skoðið terminal"

@app.route('/update')
def update():
    from tinydb import Query
    user = Query()
    db.update({'name':'Jesú', 'email':'jes@ja.kr', 'bio':'Töfrabrögð eru mín sérgrein'}, user.uid == 3 )
    # db.update({ updated field: updated information }, stable field: information)
    for i in db:
        print(i)
    return "Notandi uppfærður í db - skoðið terminal"

@app.route('/delete')
def delete():
    from tinydb import Query
    dl = Query()
    db.remove(dl.uid == 2)
    # db.remove( Query() field regex )
    return "Notandi fjarlægður úr db - skoðið terminal"
