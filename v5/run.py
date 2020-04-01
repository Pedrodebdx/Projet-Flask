from flask import Flask, render_template, request
import pymongo


app = Flask(__name__)

@app.route('/affichage_bdd')
def affichage_bdd():
    import pymongo
    # connection à mongo 
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    #création de la base de données imdb
    mydb = myclient["flaskv5"]
    #création de la collection 'titles'
    mycol = mydb["users"]
    resultat = mydb.users.find()

    liste2=[]
    for i in resultat:
        liste2.append(i)


    import pandas as pd
    # create dataframe
    df = pd.DataFrame(liste2)
    # render dataframe as html
    html = df.to_html()
    return render_template("affichage_bdd.html", html=html)

    

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
    resultat = mydb.users.find({'_id': pseudo})
    for i in resultat:
        if i['_id'] == pseudo: 
            return render_template("erreur.html")
        else:
            mycol.insert_one(data)

    return render_template("bienvenue.html", data= data)


### non fonctionel 
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      df = pd.read_csv(f)
      desc = df.describe()
      return render_template('statistics.html', tables = [desc.to_html(classes = 'data')], titles = desc.columns.values)

    return render_template("upload.html")

if __name__ == '__main__':
    app.run()






