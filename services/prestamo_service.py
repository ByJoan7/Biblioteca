# Archivo: prestamo_service.py
# Este archivo forma parte del sistema de biblioteca.
from models.prestamo import Prestamo
from utils.excepciones import UsuarioSancionadoError, MaterialNoDisponibleError



# Esta clase representa PrestamoService
class PrestamoService:

    # Constructor de la clase

    def __init__(self, materiales, usuarios, prestamos, storage_prestamos, storage_materiales):
        self.materiales = materiales
        self.usuarios = usuarios
        self.prestamos = prestamos
        self.storage_prestamos = storage_prestamos
        self.storage_materiales = storage_materiales

    # Funcion prestar_material: realiza una parte del funcionamiento del programa
    def prestar_material(self, usuario_id, material_id, dias=14):
        usuario = self.usuarios.get(usuario_id)
        material = self.materiales.get(material_id)

        if not usuario:
            raise Exception("El usuario no existe")
        if not material:
            raise Exception("El material no existe")
        if usuario.esta_sancionado():
            raise UsuarioSancionadoError("El usuario esta sancionado y no puede hacer prestamos")
        if not material.esta_disponible():
            raise MaterialNoDisponibleError("El material no esta disponible")

        material.prestar()

        prestamo = Prestamo(usuario, material, dias_prestamo=dias)
        self.prestamos.append(prestamo)

        self._guardar_prestamos()
        self._guardar_materiales()

        return prestamo

    # Funcion devolver_material: realiza una parte del funcionamiento del programa
    def devolver_material(self, material_id):
        for p in self.prestamos:
            if p.material._id == material_id and p.activo:
                p.devolver()
                p.material.devolver()
                if p.esta_vencido():
                    p.usuario.sancionar()
                self._guardar_prestamos()
                self._guardar_materiales()
                return p
        raise Exception("No hay un prestamo activo para ese material")

    # Funcion _guardar_prestamos: realiza una parte del funcionamiento del programa
    def _guardar_prestamos(self):
        data = []
        for p in self.prestamos:
            data.append(p.to_dict())
        self.storage_prestamos.guardar(data)

    # Funcion _guardar_materiales: realiza una parte del funcionamiento del programa
    def _guardar_materiales(self):
        data = []
        for m in self.materiales.values():
            data.append(m.to_dict())
        self.storage_materiales.guardar(data)