from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_cors import cross_origin
from utils.validations import *
from database import db
import math
import filetype
import hashlib
import os
from werkzeug.utils import secure_filename



UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def index():
    return render_template("index.html")
##
###
##SIMPLEMENTE PARA DEJAR LINDA LA NAVBAR
###Ahora implementamos para tarea 3
@app.route("/agregar_hincha", methods=['GET', 'POST'])
def agregar_hincha():
    if request.method == 'POST':
        nombre = request.form['nombres']
        email = request.form['email']
        numero = request.form['numero']
        region = request.form['regiones']
        comuna = request.form['comunas']
        transporte = request.form['transportes']
        deportes = request.form.getlist('deportes')
        comentarios = request.form['comentarios']
        error = ""
        if (validate_hincha(nombre,email,numero,comuna,region,transporte,deportes,comentarios)== True):
            status, msg = db.signup_hincha(comuna,transporte,nombre,email,numero,deportes,comentarios)
            if status:
                flash("Hincha agregado correctamente")
                return redirect(url_for('index'))
            error = msg
        else:
            error = "Error en los datos ingresados"
        return render_template('agregar-hincha.html', error=error)
    else:
        return render_template("agregar-hincha.html")

@app.route("/ver_hincha",defaults={'page': 1})
@app.route('/ver_hincha/<int:page>')
def ver_hincha(page):
    total_rows = db.get_rows_len_hincha()
    page_size = 5
    total_page = math.ceil(total_rows / page_size)
    next = page + 1
    prev = page - 1
    data=[]
    for hincha in db.get_hinchas((page-1)*page_size):
        id , comuna , transporte , nombre , _ , telefono = hincha
        comunas = db.get_comuna_nombre(comuna)[0]
        deportes = db.get_deportes(id)
        deportes_hincha = [db.get_deporte_nombre(deporte[0])[0] for deporte in deportes]
        data.append({
            "comuna": comunas,
            "nombre": nombre,
            "telefono": telefono,
            "transporte": transporte,
            "deportes": ", ".join(deportes_hincha),
            "id": id
        })
    return render_template("ver-hincha.html", hinchas=data, pages=total_page, next=next, prev=prev)

@app.route("/informacion_hincha/<int:id>")
def informacion_hincha(id):
    data=[]
    hincha = db.get_hincha(id)
    id_h , comuna , modo_transporte , nombre , email , celular = hincha
    comunas = db.get_comuna_nombre(comuna)[0]
    deportes = db.get_deportes(id_h)
    deportes_hincha = [db.get_deporte_nombre(deporte[0])[0] for deporte in deportes]
    data.append({
        "comuna": comunas,
        "nombre": nombre,
        "telefono": celular,
        "deportes": ", ".join(deportes_hincha),
        "transporte": modo_transporte,
        "email": email,
        "id": id_h
    })
    return render_template("informacion-hincha.html", hinchas=data)

@app.route("/stats")
def stats():
    return render_template("stats.html")

@app.route("/get-stats-data", methods=["GET"])
@cross_origin(origin="localhost", supports_credentials=True)
def get_stats():
    data = [{
        "name": db.get_deporte_nombre(id),
        "data": db.get_stats_deportes(id)
    } for id in range(1,61) if db.get_stats_deportes(id) != 0]
    data2 = [{
        "name": db.get_categoria_nombre(id),
        "data": db.get_stats_artesanias(id)
    } for id in range(1,10) if db.get_stats_artesanias(id) != 0]

    return jsonify({
        "data": data,
        "data2": data2
    })

###
## c:

@app.route('/agregar_artesano', methods=['GET', 'POST'])
def agregar_artesano():
    if request.method == 'POST':
        nombre = request.form['nombres']
        email = request.form['email']
        telefono = request.form['telefono']
        comuna = request.form['comunas']
        region = request.form['regiones']
        artesania = request.form.getlist('tipos')
        fotos = request.files.getlist('fotos')
        descripcion = request.form['descripcion']
        error = ""
        if (validate_artesano(nombre,email,telefono,comuna,region,artesania,descripcion)== True):
            status, msg = db.signup_artesano(comuna,descripcion,nombre,email,telefono,artesania)
            id = db.get_art_id(nombre)[0]
            if(validate_foto(fotos) == True):
                for foto in fotos: 
                    _filename = hashlib.sha256(
                        secure_filename(foto.filename).encode('utf-8')).hexdigest()
                    _extension = filetype.guess(foto).extension
                    img_filename = f"{_filename}.{_extension}"

                    foto.save(os.path.join(UPLOAD_FOLDER, img_filename))
                    db.signup_foto(url_for('static', filename=f"uploads/{img_filename}"),img_filename, id)
            if status:
                flash("Artesano agregado correctamente")
                return redirect(url_for('index'))
            error = msg
        else:
            error = "Error en los datos ingresados"
        return render_template('agregar-artesano.html', error=error)        
    else:
        return render_template('agregar-artesano.html')
    
@app.route('/ver_artesano', defaults={'page': 1})
@app.route('/ver_artesano/<int:page>')
def ver_artesanos(page):
    total_rows = db.get_rows_len()
    page_size = 5
    total_page = math.ceil(total_rows / page_size)
    next = page + 1
    prev = page - 1
    data=[]
    for artesano in db.get_artesanos((page-1)*page_size):
        id , comuna , _ , nombre , _ , telefono = artesano
        comunas = db.get_comuna_nombre(comuna)[0]
        tipos = db.get_tipos_artesano(id)
        tipos_artesanias = [db.get_categoria_nombre(tipo[0])[0] for tipo in tipos]
        fotos= db.get_fotos(id)
        _filenames = [foto[0] for foto in fotos]
        imgFilenames = [f"uploads/{_filename}" for _filename in _filenames]
        pathImages= [url_for('static', filename=imgFilename) for imgFilename in imgFilenames]
        data.append({
            "comuna": comunas,
            "nombre": nombre,
            "telefono": telefono,
            "tipo_artesanias": ", ".join(tipos_artesanias),
            "id": id,
            "path_images": pathImages
        })
    return render_template('ver-artesano.html', artesanos=data, pages=total_page, next=next, prev=prev)


@app.route('/informacion_artesano/<int:id>')
def informacion_artesano(id):
    data=[]
    artesano = db.get_artesano(id)
    id_a , comuna , descripcion , nombre , email , celular = artesano
    comunas = db.get_comuna_nombre(comuna)[0]
    tipos = db.get_tipos_artesano(id_a)
    tipos_artesanias = [db.get_categoria_nombre(tipo[0])[0] for tipo in tipos]
    fotos= db.get_fotos(id_a)
    _filenames = [foto[0] for foto in fotos]
    img_filenames = [f"uploads/{_filename}" for _filename in _filenames]
    path_images= [url_for('static', filename=img_filename) for img_filename in img_filenames]
    data.append({
        "comuna": comunas,
        "nombre": nombre,
        "telefono": celular,
        "tipo_artesanias": ", ".join(tipos_artesanias),
        "descripcion": descripcion,
        "email": email,
        "id": id_a,
        "path_images": path_images
    })
    return render_template('informacion-artesano.html', artesanos=data)

if __name__ == '__main__':
    app.run(port=3006, debug=True)