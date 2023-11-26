import pymysql
import cryptography


DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = 3306
DB_CHARSET = "utf8"


def get_conn():
	conn = pymysql.connect(
		db=DB_NAME,
		user=DB_USERNAME,
		passwd=DB_PASSWORD,
		host=DB_HOST,
		port=DB_PORT,
		charset=DB_CHARSET
	)
	return conn


###querys tarea 3
def get_hincha_id(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM hincha WHERE nombre=%s;", (nombre,))
    id = cursor.fetchone()
    return id
def create_hincha(comuna_id, modo_transporte, nombre, email, celular, comentarios):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO hincha (comuna_id, modo_transporte, nombre, email, celular, comentarios) VALUES (%s, %s, %s, %s, %s, %s);", (comuna_id, modo_transporte, nombre, email, celular, comentarios,))
    conn.commit()
def create_hincha_deporte(nombre, deporte_id):
    conn = get_conn()
    cursor = conn.cursor()
    hincha_id = get_hincha_id(nombre)
    for deporte in deporte_id:
        cursor.execute("INSERT INTO hincha_deporte (hincha_id, deporte_id) VALUES (%s, %s);", (hincha_id, deporte,))
    conn.commit()
def signup_hincha(comuna_id, modo_transporte, nombre, email, celular, deportes, comentarios):
    if get_hincha_id(nombre) is not None:
        return  False, "El hincha ya existe en la base de datos. ._."

    create_hincha(comuna_id, modo_transporte, nombre, email, celular, comentarios)
    create_hincha_deporte(nombre, deportes)
    return True, "El hincha ha sido registrado exitosamente! c:"

def get_rows_len_hincha():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hincha;")
    count = cursor.fetchone()
    return count[0]
def get_hinchas(page_size):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, modo_transporte, nombre, email, celular FROM hincha ORDER BY id DESC LIMIT %s, 5;", (page_size,))
    hinchas = cursor.fetchall()
    return hinchas
def get_deportes(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT deporte_id FROM hincha_deporte WHERE hincha_id=%s;", (id,))
    deportes = cursor.fetchall()
    return deportes
def get_deporte_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM deporte WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre
def get_hincha(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, modo_transporte, nombre, email, celular FROM hincha WHERE id=%s;", (id,))
    hincha = cursor.fetchone()
    return hincha
def get_stats_deportes(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM hincha_deporte WHERE deporte_id=%s;", (id,))
    count = cursor.fetchone()
    return count[0]
def get_stats_artesanias(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM artesano_tipo WHERE tipo_artesania_id=%s;", (id,))
    count = cursor.fetchone()
    return count[0]




#####

def get_art_id(nombre):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM artesano WHERE nombre=%s;", (nombre,))
    id = cursor.fetchone()
    return id

def create_artesano(comuna,descripcion,nombre,email,celular):
    conn = get_conn()
    cursor = conn.cursor()
    id = get_art_id(nombre)
    cursor.execute("INSERT INTO artesano (comuna_id, descripcion_artesania, nombre, email, celular) VALUES (%s, %s, %s, %s, %s);", (comuna, descripcion, nombre, email, celular,))
    conn.commit()

def create_artesano_tipo(nombre,tipos):
    conn = get_conn()
    cursor = conn.cursor()
    id= get_art_id(nombre)
    for tipo in tipos:
        cursor.execute("INSERT INTO artesano_tipo (artesano_id, tipo_artesania_id) VALUES (%s, %s);" , (id,tipo))
    conn.commit()

def signup_foto(foto_ruta, foto_nombre, id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO foto (ruta_archivo, nombre_archivo, artesano_id) VALUES (%s, %s, %s);", (foto_ruta, foto_nombre, id,))
    conn.commit()

def signup_artesano(comuna,descripcion,nombre,email,celular,tipos):
    if get_art_id(nombre) is not None:
        return  False, "El artesano ya existe en la base de datos. ._."

    create_artesano(comuna,descripcion,nombre,email,celular)
    create_artesano_tipo(nombre,tipos)
    return True, "El artesano ha sido registrado exitosamente! c:"

def get_categoria_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM tipo_artesania WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre


def get_rows_len():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM artesano;")
    count = cursor.fetchone()
    return count[0]

def get_tipos_artesano(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT tipo_artesania_id FROM artesano_tipo WHERE artesano_id=%s;", (id,))
    tipos = cursor.fetchall()
    return tipos

def get_artesano(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano WHERE id=%s;", (id,))
    artesano = cursor.fetchone()
    return artesano

def get_artesanos(page_size):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, comuna_id, descripcion_artesania, nombre, email, celular FROM artesano ORDER BY id DESC LIMIT %s, 5;", (page_size,))
    artesanos = cursor.fetchall()
    return artesanos

def get_comuna_nombre(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre FROM comuna WHERE id=%s;", (id,))
    nombre = cursor.fetchone()
    return nombre

def get_fotos(id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nombre_archivo FROM foto WHERE artesano_id=%s;", (id,))
    fotos = cursor.fetchall()
    return fotos
