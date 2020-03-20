from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message_home = "page 1")

@app.route("/next")

def suite():
    return render_template("page_suivante.html")

if __name__ == "__main__":
    app.run(debug=True)
