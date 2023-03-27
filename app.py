from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/bicicletas/")
def bicicletas():
 return render_template("bicicletas.html")

@app.route("/acerca_nosotros/")
def acerca_nosotros():
 return render_template("Acerca-de.html")

@app.route("/inicio/")
def inicio():
 return render_template("index.html")

@app.route("/registrobicis/")
def registrobicis():
 return render_template("registrobicis.html")

@app.route("/registrouser/")
def registrouser():
 return render_template("registrouser.html")

@app.route("/login/")
def login():
 return render_template("login.html")



if __name__ == '__main__':
    app.run()