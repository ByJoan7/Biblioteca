from datetime import datetime, timedelta

class Reserva:
    def __init__(self, usuario, material):
        self.usuario = usuario
        self.material = material
        self.fecha = datetime.now()
        self.fecha_caducidad = self.fecha + timedelta(days=7)
        self.activa = True

    def esta_caducada(self):
        return datetime.now() > self.fecha_caducidad

    def cancelar(self):
        self.activa = False

    def esta_activa(self):
        return self.activa and not self.esta_caducada()

    def descripcion_corta(self):
        estado = "ACTIVA" if self.esta_activa() else "CANCELADA"
        return f"Usuario: {self.usuario._nombre} | Material: {self.material._titulo} | Caduca: {self.fecha_caducidad.strftime('%d/%m/%Y')} | {estado}"

    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "fecha": self.fecha.isoformat(),
            "fecha_caducidad": self.fecha_caducidad.isoformat(),
            "activa": self.activa
        }
