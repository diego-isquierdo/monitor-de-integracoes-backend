from app import app


@app.route("/")
def index():
    return "HELLO"

@app.route("/test", defaults={'name':None})
@app.route("/test/<name>")
def test(name):
    if name:
        return "ola / obas %s" % name
    else:
        return "Obas Zé"
