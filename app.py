from tareas import GestorTareas
from flask import Flask, render_template, request, redirect, url_for

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
            username.append(gestor.acceder(request.form["email"], request.form("password")))
        elif username == [None]:
                username = []
                error = "Error al iniciar sesión."
        else:
            error = "Ya tienes una cuenta."
            
@app.route('/crearcuenta')
def crearcuenta():
    return render_template("register.html")

@app.route("/registrar", methods=["POST", "GET"])
def registrar():
    error = None
    if request.method == "POST":
        gestor.crear_usuario(request.form["name"], request.form["email"], request.form["password"])
        return redirect(url_for("iniciarsesion"))
    else:
        error = "No se pudo crear la cuenta"

if __name__ == '__main__':
    app.run(debug=True)