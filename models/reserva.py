# Archivo: reserva.py
# Este archivo forma parte del sistema de biblioteca.
from datetime import datetime, timedelta


# Esta clase representa Reserva
class Reserva:
    # Constructor de la clase

    def __init__(self, usuario, material):
        self.usuario = usuario
        self.material = material
        self.fecha = datetime.now()
        self.fecha_caducidad = self.fecha + timedelta(days=7)
        self.activa = True

    # Funcion esta_caducada: realiza una parte del funcionamiento del programa
    def esta_caducada(self):
        return datetime.now() > self.fecha_caducidad

    # Funcion cancelar: realiza una parte del funcionamiento del programa
    def cancelar(self):
        self.activa = False

    # Funcion esta_activa: realiza una parte del funcionamiento del programa
    def esta_activa(self):
        return self.activa and not self.esta_caducada()

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "ACTIVA" if self.esta_activa() else "CANCELADA"
        return f"Usuario: {self.usuario._nombre} | Material: {self.material._titulo} | Caduca: {self.fecha_caducidad.strftime('%d/%m/%Y')} | {estado}"

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "fecha": self.fecha.isoformat(),
            "fecha_caducidad": self.fecha_caducidad.isoformat(),
            "activa": self.activa
        }