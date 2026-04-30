class Material:
    def __init__(self, id, titulo, autor, categoria):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._disponible = True

    def esta_disponible(self):
        return self._disponible

    def prestar(self):
        self._disponible = False

    def devolver(self):
        self._disponible = True

    def to_dict(self):
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "categoria": self._categoria,
            "disponible": self._disponible
        }