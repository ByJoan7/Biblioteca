class Material:
    def __init__(self, idLib, titulo, autor, categoria, disponible=True):
        self._id = idLib
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._disponible = bool(disponible)
        self._veces_prestado = 0

    def prestar(self):
        if self._disponible:
            self._disponible = False
            self._veces_prestado += 1
            return True
        return False

    def devolver(self):
        if not self._disponible:
            self._disponible = True
            return True
        return False

    def esta_disponible(self):
        return self._disponible

    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | {self._categoria} ({estado})"

    def __repr__(self):
        return self.descripcion_corta()

    def to_dict(self):
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "categoria": self._categoria,
            "disponible": self._disponible,
            "veces_prestado": self._veces_prestado
        }
