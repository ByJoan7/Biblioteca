from .material import Material

class Libro(Material):
    def __init__(self, id, titulo, autor, categoria, isbn):
        super().__init__(id, titulo, autor, categoria)
        self._isbn = isbn

    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | ISBN: {self._isbn} | {self._categoria} ({estado})"

    def to_dict(self):
        data = super().to_dict()
        data["isbn"] = self._isbn
        data["tipo"] = "libro"
        return data
