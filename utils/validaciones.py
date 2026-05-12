def validar_id(id):
    if not id or id.strip() == "":
        raise ValueError("El ID no puede estar vacio")

def validar_texto(texto, nombre_campo):
    if not texto or texto.strip() == "":
        raise ValueError(f"El campo {nombre_campo} no puede estar vacio")

def validar_numero_positivo(numero, nombre_campo):
    if not str(numero).isdigit() or int(numero) <= 0:
        raise ValueError(f"El campo {nombre_campo} tiene que ser un numero positivo")
