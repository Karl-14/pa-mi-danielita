from flask import Flask, request, render_template
import os

app = Flask(__name__)

# Configura la carpeta de carga
UPLOAD_FOLDER = 'uploads'  # Usa solo 'uploads' porque Flask buscará en la carpeta del proyecto
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Asegúrate de que la carpeta exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ruta del archivo donde se guardarán los mensajes
MESSAGES_FILE = 'mensajes.txt'

@app.route('/')
def home():
    return render_template('boton2.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Verifica si se subieron archivos
    if 'archivo' not in request.files:
        return 'No se subió ningún archivo', 400

    files = request.files.getlist('archivo')  # Obtiene todos los archivos subidos

    for file in files:
        if file.filename == '':
            return 'Nombre de archivo no válido', 400

        # Guarda el archivo en la carpeta de uploads
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

    return '¡Carga completada!', 200

@app.route('/contact', methods=['POST'])
def contact():
    # Obtiene el mensaje del formulario de contacto
    mensaje = request.form.get('mensaje')
    
    # Guardar el mensaje en el archivo
    with open(MESSAGES_FILE, 'a') as f:
        f.write(mensaje + '\n')  # Escribir el mensaje seguido de una nueva línea

    return '¡Mensaje enviado con éxito!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)