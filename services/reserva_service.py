from models.reserva import Reserva


class ReservaService:

    def __init__(self, materiales, usuarios, reservas, storage_reservas):
        self.materiales = materiales
        self.usuarios = usuarios
        self.reservas = reservas
        self.storage_reservas = storage_reservas

    def reservar_material(self, usuario_id, material_id):
        usuario = self.usuarios.get(usuario_id)
        material = self.materiales.get(material_id)

        if not usuario:
            raise Exception("El usuario no existe")

        if not material:
            raise Exception("El material no existe")

        if usuario.esta_sancionado():
            raise Exception("El usuario esta sancionado y no puede hacer reservas")

        reserva = Reserva(usuario, material)
        self.reservas.append(reserva)
        self._guardar_reservas()

        return reserva

    def cancelar_reserva(self, usuario_id, material_id):
        for r in self.reservas:
            if r.usuario._id == usuario_id and r.material._id == material_id and r.esta_activa():
                r.cancelar()
                self._guardar_reservas()
                return True
        return False

    def obtener_reservas(self):
        reservas_activas = []
        for r in self.reservas:
            if r.esta_activa():
                reservas_activas.append(r)
        return reservas_activas

    def _guardar_reservas(self):
        data = []
        for r in self.reservas:
            data.append(r.to_dict())
        self.storage_reservas.guardar(data)
