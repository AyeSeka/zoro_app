from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def Connexion():
    return render_template("Connexion.html")

@app.route("/Accueil/")
def Accueil():
    return render_template("Accueil.html")

if __name__ == "__main__":
    app.run(debug=True)