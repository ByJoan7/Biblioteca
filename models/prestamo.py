from datetime import datetime

class Prestamo:
    def __init__(self, usuario, material):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None
        self.activo = True

    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.activo = False

    def esta_vencido(self):
        if not self.activo:
            return False
        dias = (datetime.now() - self.fecha_prestamo).days
        return dias > 14  # regla básica

    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "activo": self.activo
        }