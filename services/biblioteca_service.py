from persistence.json_storage import JSONStorage
from models.prestamo import Prestamo
from models.libro import Libro
from models.usuario import Usuario
from models.revista import Revista
from models.recurso_digital import RecursoDigital
from models.reserva import Reserva
from services.prestamo_service import PrestamoService
from services.reserva_service import ReservaService


class BibliotecaService:
    
    def __init__(self):
        self.materiales = {}
        self.usuarios = {}
        self.prestamos = []
        self.reservas = []

        self.storage_materiales = JSONStorage("data/materiales.json")
        self.storage_usuarios = JSONStorage("data/usuarios.json")
        self.storage_prestamos = JSONStorage("data/prestamos.json")
        self.storage_reservas = JSONStorage("data/reservas.json")
        self.cargar_datos()
        self.prestamo_service = PrestamoService(
            self.materiales,
            self.usuarios,
            self.prestamos,
            self.storage_prestamos,
            self.storage_materiales
        )
        self.reserva_service = ReservaService(
            self.materiales,
            self.usuarios,
            self.reservas,
            self.storage_reservas
        )

    def agregar_material(self, material):
        self.materiales[material._id] = material
        self.guardar_materiales()

    def eliminar_material(self, material_id):
        if material_id in self.materiales:
            del self.materiales[material_id]
            self.guardar_materiales()
            return True
        return False

    def modificar_material(self, material_id, nuevos_datos):
        material = self.materiales.get(material_id)
        if material:
            material._titulo = nuevos_datos.get("titulo", material._titulo)
            material._autor = nuevos_datos.get("autor", material._autor)
            material._categoria = nuevos_datos.get("categoria", material._categoria)
            if hasattr(material, "_isbn"):
                material._isbn = nuevos_datos.get("isbn", material._isbn)
            if hasattr(material, "_url"):
                material._url = nuevos_datos.get("url", material._url)
            if hasattr(material, "_numero_edicion"):
                material._numero_edicion = nuevos_datos.get("numero_edicion", material._numero_edicion)
            self.guardar_materiales()
            return True
        return False

    def buscar_materiales(self, criterio, valor):
        valor = valor.lower()
        resultados = []
        for m in self.materiales.values():
            if criterio == "titulo" and valor in m._titulo.lower():
                resultados.append(m)
            elif criterio == "autor" and valor in m._autor.lower():
                resultados.append(m)
            elif criterio == "categoria" and valor in m._categoria.lower():
                resultados.append(m)
        return resultados

    def obtener_materiales(self):
        return list(self.materiales.values())
        
    def agregar_usuario(self, usuario):
        self.usuarios[usuario._id] = usuario
        self.guardar_usuarios()

    def eliminar_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            del self.usuarios[usuario_id]
            self.guardar_usuarios()
            return True
        return False

    def modificar_usuario(self, usuario_id, nuevos_datos):
        usuario = self.usuarios.get(usuario_id)
        if usuario:
            usuario._nombre = nuevos_datos.get("nombre", usuario._nombre)
            self.guardar_usuarios()
            return True
        return False

    def obtener_usuarios(self):
        return list(self.usuarios.values())

    def prestar_material(self, usuario_id, material_id, dias=14):
        return self.prestamo_service.prestar_material(usuario_id, material_id, dias)

    def devolver_material(self, material_id):
        return self.prestamo_service.devolver_material(material_id)

    def reservar_material(self, usuario_id, material_id):
        return self.reserva_service.reservar_material(usuario_id, material_id)

    def obtener_reservas(self):
        return self.reserva_service.obtener_reservas()

    def guardar_materiales(self):
        data = [m.to_dict() for m in self.materiales.values()]
        self.storage_materiales.guardar(data)

    def guardar_usuarios(self):
        data = [u.to_dict() for u in self.usuarios.values()]
        self.storage_usuarios.guardar(data)

    def guardar_prestamos(self):
        data = [p.to_dict() for p in self.prestamos]
        self.storage_prestamos.guardar(data)

    def guardar_reservas(self):
        data = [r.to_dict() for r in self.reservas]
        self.storage_reservas.guardar(data)

    def cargar_datos(self):
        self._cargar_materiales()
        self._cargar_usuarios()
        self._cargar_prestamos()
        self._cargar_reservas()

    def _cargar_materiales(self):
        data = self.storage_materiales.cargar()
        for m in data:
            if m["tipo"] == "libro":
                material = Libro(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("isbn", ""))
            elif m["tipo"] == "revista":
                material = Revista(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("numero_edicion", 0))
            elif m["tipo"] == "digital":
                material = RecursoDigital(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("url", ""))
            else:
                continue
            if not m.get("disponible", True):
                material.prestar()
            material._veces_prestado = m.get("veces_prestado", 0)
            self.materiales[m["id"]] = material

    def _cargar_usuarios(self):
        data = self.storage_usuarios.cargar()
        for u in data:
            usuario = Usuario(u["id"], u["nombre"])
            if u.get("sancionado", False):
                usuario.sancionar()
            self.usuarios[u["id"]] = usuario

    def _cargar_prestamos(self):
        from datetime import datetime
        data = self.storage_prestamos.cargar()
        for p in data:
            usuario = self.usuarios.get(p["usuario"])
            material = self.materiales.get(p["material"])
            if usuario and material:
                prestamo = Prestamo(usuario, material)
                prestamo.activo = p.get("activo", True)
                if "fecha_prestamo" in p:
                    prestamo.fecha_prestamo = datetime.fromisoformat(p["fecha_prestamo"])
                if "fecha_vencimiento" in p:
                    prestamo.fecha_vencimiento = datetime.fromisoformat(p["fecha_vencimiento"])
                if "fecha_devolucion" in p and p["fecha_devolucion"]:
                    prestamo.fecha_devolucion = datetime.fromisoformat(p["fecha_devolucion"])
                self.prestamos.append(prestamo)

    def _cargar_reservas(self):
        data = self.storage_reservas.cargar()
        for r in data:
            u = self.usuarios.get(r["usuario"])
            m = self.materiales.get(r["material"])
            if u and m:
                reserva = Reserva(u, m)
                self.reservas.append(reserva)
