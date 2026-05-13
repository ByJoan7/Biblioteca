# Archivo: libro.py
# Este archivo forma parte del sistema de biblioteca.
from .material import Material


# Esta clase representa Libro
class Libro(Material):
    # Constructor de la clase

    def __init__(self, id, titulo, autor, categoria, isbn):
        super().__init__(id, titulo, autor, categoria)
        self._isbn = isbn

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | ISBN: {self._isbn} | {self._categoria} ({estado})"

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        data = super().to_dict()
        data["isbn"] = self._isbn
        data["tipo"] = "libro"
        return data