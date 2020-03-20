# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 15:16:04 2020

@author: utilisateur
"""


from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "coucou bla bla bla"

if __name__ == "__main__":
    app.run()