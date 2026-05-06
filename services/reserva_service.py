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

        if not usuario or not material:
            raise Exception("Usuario o material no existe")

        reserva = Reserva(usuario, material)
        self.reservas.append(reserva)
        self.guardar()

        return reserva

    def obtener_reservas(self):
        return self.reservas

    def guardar(self):
        data = [r.to_dict() for r in self.reservas]
        self.storage_reservas.guardar(data)