from .material import Material

class Revista(Material):
    def __init__(self, id, titulo, autor, categoria, numero_edicion):
        super().__init__(id, titulo, autor, categoria)
        self._numero_edicion = numero_edicion

    def to_dict(self):
        data = super().to_dict()
        data["numero_edicion"] = self._numero_edicion
        data["tipo"] = "revista"
        return data