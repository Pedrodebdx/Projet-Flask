from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message = " Bla bla  youhouuu  ")

if __name__ == "__main__":
    app.run()



