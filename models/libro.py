from .material import Material

class Libro(Material):
    def __init__(self, id, titulo, autor, isbn):
        super().__init__(id, titulo, autor)
        self._isbn = isbn

    def to_dict(self):
        data = super().to_dict()
        data["isbn"] = self._isbn
        data["tipo"] = "libro"
        return data
