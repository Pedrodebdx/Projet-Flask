from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    nom = request.form['nom'].upper()
    prenom = request.form['prenom']
    age = request.form['age']
    sexe = request.form['sexe']
    
    
    
    return render_template("bienvenue.html", 
    prenom=prenom, nom=nom, age=age, sexe=sexe)

if __name__ == '__main__':
    app.run()