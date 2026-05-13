# Archivo: revista.py
# Este archivo forma parte del sistema de biblioteca.
from .material import Material


# Esta clase representa Revista
class Revista(Material):
    # Constructor de la clase

    def __init__(self, id, titulo, autor, categoria, numero_edicion):
        super().__init__(id, titulo, autor, categoria)
        self._numero_edicion = int(numero_edicion)

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._titulo} - {self._autor} | Nro {self._numero_edicion} | {self._categoria} ({estado})"

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        data = super().to_dict()
        data["numero_edicion"] = self._numero_edicion
        data["tipo"] = "revista"
        return data