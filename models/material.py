class Material:
    def __init__(self, idLib, titulo, autor, categoria, disponible=True):
        self._id = idLib
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._disponible = disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
        else:
            return "Material no disponible para prestar."

    def devolver(self):
        if not self._disponible:
            self._disponible = True
        else:           
            return "Material ya está disponible."

    def desc_lib(self):
        if self._disponible:
            estado = "Disponible"
        else:            
            estado = "No disponible"
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "categoria": self._categoria,
            "disponible": self._disponible
        }
    
