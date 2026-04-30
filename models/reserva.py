from datetime import datetime

class Reserva:
    def __init__(self, usuario, material):
        self.usuario = usuario
        self.material = material
        self.fecha = datetime.now()

    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "fecha": str(self.fecha)
        }