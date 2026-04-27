from tareas import GestorTareas, ejemplo_uso
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = "secreto"
usuario = None

@app.route('/')
def index():
    global usuario
    if usuario != None:
        return redirect(url_for("gestor"))
    return render_template("index.html")

@app.route("/iniciarsesion", methods=["POST", "GET"])
def iniciarsesion():
    gestor = GestorTareas()
    global usuario
    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password")
        usuario = gestor.acceder(email, password)
        if usuario != None:
            return redirect(url_for("gestor"))
        elif usuario == None:
            flash("Error al iniciar sesión", "error")
            return redirect(url_for("index"))
        else:
            flash("Ya tienes una cuenta", "error")
            return redirect(url_for("index"))
            
@app.route('/crearcuenta')
def crearcuenta():
    if usuario != None:
        return redirect(url_for("gestor"))
    return render_template("register.html")

@app.route("/registrar", methods=["POST", "GET"])
def registrar():
    error = None
    gestor = GestorTareas()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        gestor.crear_usuario(name, email, password)
        return redirect(url_for("index"))
    else:
        flash("No se pudo crear la cuenta", "error")
        return redirect(url_for("crearcuenta"))
        
@app.route("/gestor")
def gestor():
    return render_template("gestor.html")

if __name__ == '__main__':
    #ejemplo_uso()
    app.run(debug=True)