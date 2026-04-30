from .material import Material

class RecursoDigital(Material):
    def __init__(self, id, titulo, autor, categoria, url):
        super().__init__(id, titulo, autor, categoria)
        self._url = url

    def to_dict(self):
        data = super().to_dict()
        data["url"] = self._url
        data["tipo"] = "digital"
        return data