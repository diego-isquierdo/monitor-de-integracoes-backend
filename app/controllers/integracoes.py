from app import app

@app.route("/integracoes", methods=['GET'])
def integracoes():
    return "INTEGRACOES"