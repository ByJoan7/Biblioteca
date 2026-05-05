class Usuario:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre
        self._sancionado = False
        self._prestamos_activos = 0

    def esta_sancionado(self):
        return self._sancionado

    def sancionar(self):
        self._sancionado = True

    def levantar_sancion(self):
        self._sancionado = False

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "sancionado": self._sancionado
        }
    def buscar_por_nombre(usuarios, nombre):
    resultado = []
    for usuario in usuarios:
        if nombre.lower() in usuario._nombre.lower():
            resultado.append(usuario)
    return resultado
