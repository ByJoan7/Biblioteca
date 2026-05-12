from models.prestamo import Prestamo

class PrestamoService:

    def __init__(self, materiales, usuarios, prestamos, storage_prestamos, storage_materiales):
        self.materiales = materiales
        self.usuarios = usuarios
        self.prestamos = prestamos
        self.storage_prestamos = storage_prestamos
        self.storage_materiales = storage_materiales

    def prestar_material(self, usuario_id, material_id, dias=14):
        usuario = self.usuarios.get(usuario_id)
        material = self.materiales.get(material_id)

        if not usuario or not material:
            raise Exception("Usuario o material no existe")

        if usuario.esta_sancionado():
            raise Exception("Usuario sancionado")

        if not material.esta_disponible():
            raise Exception("Material no disponible")

        material.prestar()

        prestamo = Prestamo(usuario, material, dias_prestamo=int(dias))
        self.prestamos.append(prestamo)

        self.guardar()
        return prestamo

    def devolver_material(self, material_id):
        for p in self.prestamos:
            if p.material._id == material_id and p.activo:
                p.devolver()
                p.material.devolver()
                self.guardar()
                return

        raise Exception("Prestamo no encontrado")

    def guardar(self):
        data = [p.to_dict() for p in self.prestamos]
        self.storage_prestamos.guardar(data)

        data_mat = [m.to_dict() for m in self.materiales.values()]
        self.storage_materiales.guardar(data_mat)
