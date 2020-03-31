from flask import Flask, render_template, request
import pymongo


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def text_box():
    nom = request.form['nom'].upper()
    prenom = request.form['prenom']
    pseudo = request.form['pseudo']
    #données récoltées 
    data = {'nom': nom, 'prenom':prenom, '_id': pseudo, 'pseudo': pseudo}

    import pymongo
    # connection à mongo 
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #création de la base de données imdb
    mydb = myclient["flaskv5"]
    #création de la collection 'titles'
    mycol = mydb["users"]
    #insertion des données
    
    if data['pseudo'] == mycol.find({ "_id": pseudo }) :
        return render_template("erreur.html")
    else:
        x = mycol.insert_one(data)

    return render_template("bienvenue.html", data= data)



if __name__ == '__main__':
    app.run()