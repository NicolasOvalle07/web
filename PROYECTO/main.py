from flask import Flask, render_template

xbox=Flask(__name__)

@xbox.route('/')
def ppal():
    return render_template("layout.html")

@xbox.route('/inicio')
def inicio():
    return render_template("index.html")

@xbox.route('/beneficios')
def beneficios():
    return render_template("beneficios.html")

@xbox.route('/reseñas')
def reseñas():
    return render_template("reseñas.html")

@xbox.route('/productos')
def productos():
    return render_template("productos.html")

if __name__=='__main__':
    xbox.run(debug=True)