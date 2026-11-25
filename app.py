from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form["nombre"]
        edad = int(request.form["edad"])
        cantidad = int(request.form["cantidad"])

        total = 9000 * cantidad

        if edad > 30:
            descuento = total * 0.25
        elif edad >= 18:
            descuento = total * 0.15
        else:
            descuento = 0

        pagar = total - descuento
        return render_template("ejercicio1.html", nombre=nombre, total=total,
                               descuento=descuento, pagar=pagar)

    return render_template("ejercicio1.html")


@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    if request.method == "POST":
        usuario = request.form["usuario"]
        clave = request.form["clave"]

        if usuario == "alan" and clave == "neira":
            mensaje = "Bienvenido Admin Alan"
        elif usuario == "javier" and clave == "bustos":
            mensaje = "Bienvenido Usuario Javier"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        return render_template("ejercicio2.html", mensaje=mensaje)

    return render_template("ejercicio2.html")


if __name__ == "__main__":
    app.run(debug=True)
