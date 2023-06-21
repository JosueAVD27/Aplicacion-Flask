#Importamos las librerias
from flask import Flask, redirect, render_template, request, url_for
#Intanciar la aplicacion
app = Flask(__name__, template_folder='templates')

#Array donde almacenaremos los datos
lista_tarea = []

# Variable global para almacenar el ID actual
current_id = 1

#Decorador para definir la ruta
@app.route('/')
def index():
    return render_template('inicio.html', lista_tarea = lista_tarea)

#Controlador de la ruta de envio de datos
@app.route('/enviar', methods=['POST'])                             
def enviar():                                                       #crea la funcion enviar
    if request.method == 'POST':                                    #Condicion que solicita que el metodo sea igual a post
        descripcion_tarea = request.form['descripcion_tarea']       #Extrae los datos ingresados en el input de la descripcion de la tarea
        email_tarea = request.form['email_tarea']                   #Extrae los datos ingresados en el input del correo electronico
        prioridad_tarea = request.form['prioridad_tarea']           #Extrae los datos ingresados en el input de la prioridad
        #Crea la condicion de que no guarde el registro cuando el campo de la tarea y el del correo estan vacios
        if descripcion_tarea == '' or email_tarea == '' or prioridad_tarea == '':            
            return redirect(url_for('index'))                       
        else:
            #Agrega a la lista los campos llenos
            global current_id
            lista_tarea.append({'id': current_id, 'descripcion_tarea': descripcion_tarea, 'email_tarea': email_tarea, 'prioridad_tarea': prioridad_tarea })
            current_id += 1
            return redirect(url_for('index'))

#Controlador de la ruta para borrar los datos de la tabla
@app.route('/borrar', methods=['POST'])
def borrar():                                                       #Crea la funcion de borrar la lista creada
    if request.method == 'POST':                                    #solicita al metodo post
        if lista_tarea == []:                                       #crea la condicional de la lista vacia
            return redirect(url_for('index'))                       #Si la lista esta vacia ejecuta el index
        else:
            lista_tarea.clear()                                     #Elimina toda la lista
            return redirect(url_for('index'))                       #Ejecuta el index
        

#Controlador para borrar por id
@app.route('/borrar/<int:id>', methods=['POST'])
def eliminar(id):
    if request.method == 'POST':
        global lista_tarea
        lista_tarea = [tarea for tarea in lista_tarea if tarea['id'] != id]
        return redirect(url_for('index'))

#main del programa
if __name__ == '__main__':
    app.run(debug=True)     #debug para reiniciar el servidor