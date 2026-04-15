from tareas import GestorTareas
from flask import Flask, render_template, request

app = Flask(__name__)
username = []
gestor = GestorTareas()

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/iniciarsesion", methods=["POST", "GET"])
def iniciarsesion():
    error = None
    global username
    if request.method == "POST":
        if username == []:
            username.append(gestor.acceder(request.form["email"]))
            if username == [None]:
                username = []
                error = "Error al iniciar sesión."

if __name__ == '__main__':
    app.run(debug=True)