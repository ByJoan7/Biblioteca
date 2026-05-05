from datetime import datetime, timedelta

class Prestamo:
    def __init__(self, usuario, material, dias_prestamo=14):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None
        self.activo = True

    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.activo = False

    def esta_vencido(self):
        if not self.activo:
            return self.fecha_devolucion > self.fecha_vencimiento
        return datetime.now() > self.fecha_vencimiento

    def calcular_multa(self):
        if not self.esta_vencido():
            return 0
        
        fecha_final = self.fecha_devolucion if not self.activo else datetime.now()
        dias_retraso = (fecha_final - self.fecha_vencimiento).days
        return max(0, dias_retraso * 2.0)  # 2 euros por día de retraso

    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_vencimiento": self.fecha_vencimiento.isoformat(),
            "fecha_devolucion": self.fecha_devolucion.isoformat() if self.fecha_devolucion else None,
            "activo": self.activo
        }