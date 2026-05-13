# Archivo: material.py
# Este archivo forma parte del sistema de biblioteca.

# Esta clase representa Material
class Material:
    # Constructor de la clase

    def __init__(self, idLib, titulo, autor, categoria, disponible=True):
        self._id = idLib
        self._titulo = titulo
        self._autor = autor
        self._categoria = categoria
        self._disponible = bool(disponible)
        self._veces_prestado = 0

    # Funcion prestar: realiza una parte del funcionamiento del programa
    def prestar(self):
        if self._disponible:
            self._disponible = False
            self._veces_prestado += 1
            return True
        return False

    # Funcion devolver: realiza una parte del funcionamiento del programa
    def devolver(self):
        if not self._disponible:
            self._disponible = True
            return True
        return False

    # Funcion esta_disponible: realiza una parte del funcionamiento del programa
    def esta_disponible(self):
        return self._disponible

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | {self._categoria} ({estado})"

    # Funcion __repr__: realiza una parte del funcionamiento del programa
    def __repr__(self):
        return self.descripcion_corta()

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        return {
            "id": self._id,
            "titulo": self._titulo,
            "autor": self._autor,
            "categoria": self._categoria,
            "disponible": self._disponible,
            "veces_prestado": self._veces_prestado
        }