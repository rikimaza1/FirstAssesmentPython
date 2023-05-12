from flask import Flask, request, render_template

from clases.Coches import Ford, Honda, Toyota

app = Flask(__name__, template_folder='html')


@app.route("/")
def coches():
    return render_template("start_coches.html")


@app.route("/coches", methods=['POST'])
def mostrar_coches():
    # Obtener el coche seleccionado por el usuario
    fabricante = request.form.get('coche')
    anyo = request.form["anyo"]
    modelo = request.form["modelo"]
    print(fabricante)
    print(anyo)
    print(modelo)

    # Insertar el código aquí
    if fabricante == "Ford" or fabricante == "ford":
        color = request.form["color"]
        ford = Ford(fabricante, anyo, modelo, color)
        coche_ingresado = ford
    elif fabricante == "Toyota" or fabricante == "toyota":
        num_puertas = request.form["num_puertas"]
        toyota = Toyota(fabricante, anyo, modelo, num_puertas)
        coche_ingresado = toyota
    elif fabricante == "Honda" or fabricante == "honda":
        tipo_transmision = request.form["tipo_transmision"]
        honda = Honda(fabricante, anyo, modelo, tipo_transmision)
        coche_ingresado = honda
    # Renderizar la página de coches con el coche seleccionado
    return render_template("coches.html", coche=coche_ingresado)


if __name__ == '__main__':
    app.run(debug=True)
