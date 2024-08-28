import os
from flask import Flask, render_template, request, flash, redirect
from datetime import datetime as dt

#Directorio donde se subirán las imágenes
UPLOAD_FOLDER = 'static/uploads/'

#Extensiones de imagenes permitidas
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']

app = Flask(__name__, static_folder = "static", template_folder='templates')

# Configuraciones de la app 
app.config['SECRET_KEY']= 'YourSecretKey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':

        #Verificamos que venga el archivo de imagen
        if 'file' not in request.files:
            flash('No viene ninguna imagen')
            return redirect(request.url)
        
        image = request.files['file']

        if image.filename == '':
            flash('Ninguna imagen seleccionada')
            return redirect(request.url)
        
        #Verificamos que la imagen venga y tenga la extensión permitida
        if image and image.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS:
            
            dt_now = dt.now().strftime("%Y%m%d%H%M%S%f") #para el nombre de la imagen
            image_name = dt_now + '.jpg'
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))

            img_dir = './static/uploads'
            path_img = img_dir + image_name

            return render_template('index.html', path_img = path_img)
        
if __name__ == '__main__':
    app.run()
