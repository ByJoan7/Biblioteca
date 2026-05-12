from .material import Material

class RecursoDigital(Material):
    def __init__(self, id, titulo, autor, categoria, url, formato="ebook"):
        super().__init__(id, titulo, autor, categoria)
        self._url = url
        self._formato = formato

    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | {self._formato} | {self._categoria} ({estado})"

    def to_dict(self):
        data = super().to_dict()
        data["url"] = self._url
        data["formato"] = self._formato
        data["tipo"] = "digital"
        return data
