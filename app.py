from tareas import GestorTareas, ejemplo_uso
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
username = []

@app.route('/')
def index():
    if username != []:
        return redirect(url_for("gestor"))
    return render_template("index.html")

@app.route("/iniciarsesion", methods=["POST", "GET"])
def iniciarsesion():
    gestor = GestorTareas()
    global username
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password")
        if username == []:
            username.append(gestor.acceder(email, password))
            return redirect(url_for("gestor"))
        elif username == None:
                username = []
                flash("Error al iniciar sesión", "error")
        else:
            flash("Ya tienes una cuenta", "error")
            
@app.route('/crearcuenta')
def crearcuenta():
    if username != []:
        return redirect(url_for("gestor"))
    return render_template("register.html")

@app.route("/registrar", methods=["POST", "GET"])
def registrar():
    error = None
    gestor = GestorTareas()
    if request.method == "POST":
        name = str(request.form["name"])
        email = str(request.form["email"])
        password = str(request.form["password"])
        gestor.crear_usuario(name, email, password)
        return redirect(url_for("iniciarsesion"))
    else:
        error = "No se pudo crear la cuenta"
        
@app.route("/gestor")
def gestor():
    return render_template("gestor.html")

if __name__ == '__main__':
    ejemplo_uso
    app.run(debug=True)