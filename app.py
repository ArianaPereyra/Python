from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulación de una lista de productos
lista_productos = [
    {"nombre": "Producto 1", "categoria": "Categoría A", "precio": 10.0},
    {"nombre": "Producto 2", "categoria": "Categoría B", "precio": 15.5},
    {"nombre": "Producto 3", "categoria": "Categoría A", "precio": 7.25},
    {"nombre": "Producto 4", "categoria": "Categoría C", "precio": 22.0}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/productos')
def productos():
    return render_template('/productos.html', productos=lista_productos)

@app.route('/agregar/producto', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = float(request.form['precio'])
        nuevo_producto = {"nombre": nombre, "categoria": categoria, "precio": precio}
        lista_productos.append(nuevo_producto)
        return redirect(url_for('productos'))
    return render_template('add_productos.html')

if __name__ == '__main__':
    app.run(debug=True)
