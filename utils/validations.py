import filetype

def validate_foto(foto):
    length = len(foto)
    if length == 0:
        return False
    if length > 3:
        return False
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}
    for i in range(length):
    # check if a file was submitted
        if foto[i] is None:
            return False
    # check if the browser submitted an empty file
        if foto[i].filename == "":
            return False 
    # check file extension
        ftype_guess = filetype.guess(foto[i])
        if ftype_guess.extension not in ALLOWED_EXTENSIONS:
            return False
    # check mimetype
        if ftype_guess.mime not in ALLOWED_MIMETYPES:
            return False
    return True
def validate_nombre(nombre):
    if len(nombre) == 0:
        return False
    if len(nombre) > 80:
        return False
    return True
def validate_email(email):
    if len(email) == 0:
        return False
    if len(email) > 80:
        return False
    if not "@" in email:
        return False
    return True
def validate_telefono(numero):
    if (len(numero) == 0):
        return True
    numero = numero.replace(" ", "")
    if len(numero) != 9:
        return False
    if not numero.isdigit():
        return False
    return True
def validate_region(region):
    if len(region) == 0:
        return False
    if int(region) < 1 or int(region) > 16:
        return False
    return True
def validate_comuna(comuna):
    if len(comuna) == 0:
        return False
    if int(comuna) < 10101 or int(comuna) > 130606:
        return False
    return True
def validate_tipos(tipos):
    if len(tipos) == 0:
        return False
    if len(tipos) > 3:
        return False
    for tipo in tipos:
        if int(tipo) > 9 or int(tipo) < 1:
            return False
    return True
def validate_descripcion(descripcion):
    if len(descripcion) > 300:
        return False
    return True
def validate_telefono_hincha(numero):
    numero = numero.replace(" ", "")
    if len(numero) != 9:
        return False
    if not numero.isdigit():
        return False
    return True
def validate_deportes(deportes):
    if len(deportes) == 0:
        return False
    if len(deportes) > 3:
        return False
    for deporte in deportes:
        if int(deporte) > 60 or int(deporte) < 1:
            return False
    return True
def validate_comentarios(comentarios):
    if len(comentarios) > 80:
        return False
    return True
def validate_transporte(transporte):
    if len(transporte) == 0:
        return False
    return True
def validate_artesano(nombre,email,telefono,comuna,region,tipos,descripcion):
    if not validate_nombre(nombre):
        return False
    if not validate_email(email):
        return False
    if not validate_telefono(telefono):
        return False
    if not validate_region(region):
        return False
    if not validate_comuna(comuna):
        return False
    if not validate_tipos(tipos):
        return False
    if not validate_descripcion(descripcion):
        return False
    return True

def validate_hincha(nombre, email, telefono, comuna, region,transporte, deportes, comentarios):
    if not validate_nombre(nombre):
        return False
    if not validate_email(email):
        return False
    if not validate_telefono_hincha(telefono): ##Aca es obligatorio el telefono
        return False
    if not validate_region(region):
        return False
    if not validate_comuna(comuna):
        return False
    if not validate_deportes(deportes):
        return False
    if not validate_comentarios(comentarios):
        return False
    if not validate_transporte(transporte):
        return False
    return True