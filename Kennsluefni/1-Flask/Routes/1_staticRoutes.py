from flask import Flask
app = Flask(__name__)

# You can bind more than one route to a single callback (Chaining Decorators)
@app.route('/')
@app.route('/index')
def demo1():
    return "Halló Heimur! index"

# undirsíða
@app.route('/demo2')
def demo2():
    # skilum textastreng í vafra
    return "Halló Heimur! demo2"

# blöndum saman html elementum og texta í streng sem við skilum.
@app.route('/demo3')
def demo3():
    return "<h1>Halló Heimur! demo3</h1>"

# Við getum skilað html vefsíðu sem streng
@app.route('/demo4')
def demo4():
    # breyta sem geymir html í strengjaformi
    html = '''
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
          <h1>Halló</h1>
          <a href="/sida1">Tengill</a>  <!-- tengill á routið (undirsíða) /sida1 -->
    </body>
    '''
    return html


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  


   
