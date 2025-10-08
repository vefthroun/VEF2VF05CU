# Simple Guide: Deploy a Small Database‑Backed Flask App on PythonAnywhere

## 1. Sign Up / Log In
Go to https://www.pythonanywhere.com (PAW) and create a (free) account.

![PAW free account](plan.png)

## 3. Create Your Database

- TinyDB: Just keep data/db.json in your project.

## 4. Upload Code to PythonAnywhere
Options:
- Upload files via “Files” tab
- Or start a Bash console on PAW

Keep a structure like:
 - yourproject/
    - app.py
    - requirements.txt
    - templates/
    - static/
    - data/

## 5. Create requirements.txt
In your local env:
pip freeze > requirements.txt
(Ensure it contains flask and any DB libs.)

Upload that file too.

## 6. Create a Virtualenv on PythonAnywhere
In a Bash console:
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

## 7. Start a New Web App
1. Web tab > Add a new web app.
2. Choose: Manual configuration (Flask).
3. Select the same Python version as your virtualenv.
4. After creation, set the Virtualenv path (e.g. /home/yourusername/yourproject/venv).

## 8. Configure WSGI File
Open the WSGI configuration file (link on Web tab) and edit:
Example (adjust username and paths):
import sys, os
project_path = "/home/yourusername/yourproject"
if project_path not in sys.path:
    sys.path.append(project_path)

from app import app as application
Set any environment variables if needed before import.

## 9. Flask App Structure Example
app.py (TinyDB example):
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "change_me"

db_path = os.path.join("data", "posts.json")
os.makedirs("data", exist_ok=True)
db = TinyDB(db_path)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        if title and body:
            db.insert({"title": title, "body": body})
        return redirect(url_for("index"))
    posts = db.all()
    return render_template("index.html", posts=posts)

Index template (templates/index.html):
<!doctype html>
<title>Posts</title>
<h1>Posts</h1>
<form method="post">
  <input name="title" placeholder="Title" required>
  <input name="body" placeholder="Body" required>
  <button>Add</button>
</form>
<ul>
  {% for p in posts %}
    <li><strong>{{ p.title }}</strong>: {{ p.body }}</li>
  {% endfor %}
</ul>

## 10. Reload Web App
Go to Web tab > press Reload.

## 11. View Logs
- Error log and server log available on Web tab.
- Use them to debug import errors or missing modules.

## 12. Common Fixes
- 500 error: Check error log for missing module or bad path.
- Module not found: Did you install inside the correct virtualenv?
- Template not found: Ensure templates/ folder is beside app.py.

## 13. Updating Code
Re-upload or git pull changes, then press Reload.

## 14. Simple DB Migration Note
For SQLite + SQLAlchemy: run a console, import your models, create tables:
python
>>> from app import db
>>> db.create_all()
Exit and reload.

## 15. Security Quick Tips
- Never keep real secrets in code (use environment variables for production).
- Change SECRET_KEY to a long random string.

## 16. Clean Up
Remove test prints and debug=True in production.

You now have a basic database-backed Flask site running on PythonAnywhere.

https://blog.pythonanywhere.com/121