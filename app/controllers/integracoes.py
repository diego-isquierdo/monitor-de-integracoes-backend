from flask import render_template
from app import app


@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/integracoes")
def integracoes():
    return render_template("integracoes.html")