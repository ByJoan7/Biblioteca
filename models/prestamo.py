# Archivo: prestamo.py
# Este archivo forma parte del sistema de biblioteca.
from datetime import datetime, timedelta


# Esta clase representa Prestamo
class Prestamo:
    # Constructor de la clase

    def __init__(self, usuario, material, dias_prestamo=14):
        self.usuario = usuario
        self.material = material
        self.fecha_prestamo = datetime.now()
        self.fecha_vencimiento = self.fecha_prestamo + timedelta(days=dias_prestamo)
        self.fecha_devolucion = None
        self.activo = True

    # Funcion devolver: realiza una parte del funcionamiento del programa
    def devolver(self):
        self.fecha_devolucion = datetime.now()
        self.activo = False

    # Funcion esta_vencido: realiza una parte del funcionamiento del programa
    def esta_vencido(self):
        if not self.activo:
            return self.fecha_devolucion > self.fecha_vencimiento
        return datetime.now() > self.fecha_vencimiento

    # Funcion calcular_multa: realiza una parte del funcionamiento del programa
    def calcular_multa(self):
        if not self.esta_vencido():
            return 0
        fecha_final = self.fecha_devolucion if not self.activo else datetime.now()
        dias_retraso = (fecha_final - self.fecha_vencimiento).days
        return max(0, dias_retraso * 2.0)

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "ACTIVO" if self.activo else "DEVUELTO"
        multa = self.calcular_multa()
        texto = f"Usuario: {self.usuario._nombre} | Material: {self.material._titulo} | Vence: {self.fecha_vencimiento.strftime('%d/%m/%Y')} | {estado}"
        if multa > 0:
            texto += f" | Multa: {multa:.2f} euros"
        return texto

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        return {
            "usuario": self.usuario._id,
            "material": self.material._id,
            "fecha_prestamo": self.fecha_prestamo.isoformat(),
            "fecha_vencimiento": self.fecha_vencimiento.isoformat(),
            "fecha_devolucion": self.fecha_devolucion.isoformat() if self.fecha_devolucion else None,
            "activo": self.activo
        }