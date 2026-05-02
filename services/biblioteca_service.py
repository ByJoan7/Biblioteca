from persistence.json_storage import JSONStorage
from models.prestamo import Prestamo
from models.libro import Libro
from models.usuario import Usuario


class BibliotecaService:

    # =========================================================
    # 1. INICIALIZACIÓN
    # =========================================================

    def __init__(self):
        self.materiales = {}
        self.usuarios = {}
        self.prestamos = []

        # Storage
        self.storage_materiales = JSONStorage("data/materiales.json")
        self.storage_usuarios = JSONStorage("data/usuarios.json")
        self.storage_prestamos = JSONStorage("data/prestamos.json")

        self.cargar_datos()

    # =========================================================
    # 2. API PÚBLICA - MATERIALES
    # =========================================================

    def agregar_material(self, material):
        self.materiales[material._id] = material
        self.guardar_materiales()

    def obtener_materiales(self):
        return list(self.materiales.values())

    # =========================================================
    # 3. API PÚBLICA - USUARIOS
    # =========================================================

    def agregar_usuario(self, usuario):
        self.usuarios[usuario._id] = usuario
        self.guardar_usuarios()

    def obtener_usuarios(self):
        return list(self.usuarios.values())

    # =========================================================
    # 4. API PÚBLICA - PRÉSTAMOS
    # =========================================================

    def prestar_material(self, usuario_id, material_id):
        usuario = self.usuarios.get(usuario_id)
        material = self.materiales.get(material_id)

        if not usuario or not material:
            raise Exception("Usuario o material no existe")

        if usuario.esta_sancionado():
            raise Exception("Usuario sancionado")

        if not material.esta_disponible():
            raise Exception("Material no disponible")

        material.prestar()

        prestamo = Prestamo(usuario, material)
        self.prestamos.append(prestamo)

        self.guardar_prestamos()
        self.guardar_materiales()

        return prestamo

    def devolver_material(self, material_id):
        for p in self.prestamos:
            if p.material._id == material_id and p.activo:
                p.devolver()
                p.material.devolver()

                self.guardar_prestamos()
                self.guardar_materiales()
                return

        raise Exception("Préstamo no encontrado")

    # =========================================================
    # 5. PERSISTENCIA (GUARDAR)
    # =========================================================

    def guardar_materiales(self):
        data = [m.to_dict() for m in self.materiales.values()]
        self.storage_materiales.guardar(data)

    def guardar_usuarios(self):
        data = [u.to_dict() for u in self.usuarios.values()]
        self.storage_usuarios.guardar(data)

    def guardar_prestamos(self):
        data = [p.to_dict() for p in self.prestamos]
        self.storage_prestamos.guardar(data)

    # =========================================================
    # 6. CARGA DE DATOS
    # =========================================================

    def cargar_datos(self):
        self._cargar_materiales()
        self._cargar_usuarios()

    # ----------------- PRIVADO: MATERIALES -----------------
    def _cargar_materiales(self):
        data = self.storage_materiales.cargar()

        for m in data:
            if m["tipo"] == "libro":
                material = Libro(
                    m["id"],
                    m["titulo"],
                    m["autor"],
                    m["categoria"],
                    m.get("isbn", "")
                )
            else:
                continue

            # Restaurar disponibilidad
            if not m.get("disponible", True):
                material.prestar()

            self.materiales[m["id"]] = material

    # ----------------- PRIVADO: USUARIOS -----------------
    def _cargar_usuarios(self):
        data = self.storage_usuarios.cargar()

        for u in data:
            usuario = Usuario(
                u["id"],
                u["nombre"],
                u["tipo"]
            )

            if u.get("sancionado", False):
                usuario.sancionar()

            self.usuarios[u["id"]] = usuario