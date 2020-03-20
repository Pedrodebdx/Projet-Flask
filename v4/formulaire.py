from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    nom = request.form['nom']
    prenom = request.form['prenom']
    taille = request.form['taille']
    sexe = request.form['sexe']
    processed_nom = nom.upper()
    processed_prenom = prenom.upper()
    
    
    return render_template("bienvenue.html", message=processed_text)

if __name__ == '__main__':
    app.run()