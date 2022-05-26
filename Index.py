#Importamos las librerias
from flask import Flask, render_template

#Intanciar la aplicacion
app = Flask(__name__, template_folder='templates')



#Decorador para definir la ruta
@app.route('/')
def index():
    return render_template('inicio.html')



#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor