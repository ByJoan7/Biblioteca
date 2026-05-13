# Archivo: biblioteca_service.py
# Este archivo forma parte del sistema de biblioteca.
from persistence.json_storage import JSONStorage
from models.prestamo import Prestamo
from models.libro import Libro
from models.usuario import Usuario, Socio, Bibliotecario, Administrador
from models.revista import Revista
from models.recurso_digital import RecursoDigital
from models.reserva import Reserva
from services.prestamo_service import PrestamoService
from services.reserva_service import ReservaService



# Esta clase representa BibliotecaService
class BibliotecaService:

    # Constructor de la clase

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
            self.materiales, self.usuarios, self.prestamos,
            self.storage_prestamos, self.storage_materiales
        )
        self.reserva_service = ReservaService(
            self.materiales, self.usuarios, self.reservas,
            self.storage_reservas
        )

    # MATERIALES

    # Funcion agregar_material: realiza una parte del funcionamiento del programa
    def agregar_material(self, material):
        self.materiales[material._id] = material
        self.guardar_materiales()

    # Funcion eliminar_material: realiza una parte del funcionamiento del programa
    def eliminar_material(self, material_id):
        if material_id in self.materiales:
            del self.materiales[material_id]
            self.guardar_materiales()
            return True
        return False

    # Funcion modificar_material: realiza una parte del funcionamiento del programa
    def modificar_material(self, material_id, nuevos_datos):
        material = self.materiales.get(material_id)
        if not material:
            return False
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

    # Funcion obtener_materiales: realiza una parte del funcionamiento del programa
    def obtener_materiales(self):
        return list(self.materiales.values())

    # Funcion buscar_materiales: realiza una parte del funcionamiento del programa
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

    # USUARIOS

    # Funcion agregar_usuario: realiza una parte del funcionamiento del programa
    def agregar_usuario(self, usuario):
        self.usuarios[usuario._id] = usuario
        self.guardar_usuarios()

    # Funcion eliminar_usuario: realiza una parte del funcionamiento del programa
    def eliminar_usuario(self, usuario_id):
        if usuario_id in self.usuarios:
            del self.usuarios[usuario_id]
            self.guardar_usuarios()
            return True
        return False

    # Funcion modificar_usuario: realiza una parte del funcionamiento del programa
    def modificar_usuario(self, usuario_id, nuevos_datos):
        usuario = self.usuarios.get(usuario_id)
        if not usuario:
            return False
        usuario._nombre = nuevos_datos.get("nombre", usuario._nombre)
        usuario._telefono = nuevos_datos.get("telefono", usuario._telefono)
        self.guardar_usuarios()
        return True

    # Funcion obtener_usuarios: realiza una parte del funcionamiento del programa
    def obtener_usuarios(self):
        return list(self.usuarios.values())

    # PRESTAMOS

    # Funcion prestar_material: realiza una parte del funcionamiento del programa
    def prestar_material(self, usuario_id, material_id, dias=14):
        return self.prestamo_service.prestar_material(usuario_id, material_id, dias)

    # Funcion devolver_material: realiza una parte del funcionamiento del programa
    def devolver_material(self, material_id):
        return self.prestamo_service.devolver_material(material_id)

    # RESERVAS

    # Funcion reservar_material: realiza una parte del funcionamiento del programa
    def reservar_material(self, usuario_id, material_id):
        return self.reserva_service.reservar_material(usuario_id, material_id)

    # Funcion cancelar_reserva: realiza una parte del funcionamiento del programa
    def cancelar_reserva(self, usuario_id, material_id):
        return self.reserva_service.cancelar_reserva(usuario_id, material_id)

    # Funcion obtener_reservas: realiza una parte del funcionamiento del programa
    def obtener_reservas(self):
        return self.reserva_service.obtener_reservas()

    # INFORMES

    # Funcion informe_materiales_disponibles: realiza una parte del funcionamiento del programa
    def informe_materiales_disponibles(self):
        resultado = []
        for m in self.materiales.values():
            if m.esta_disponible():
                resultado.append(m)
        return resultado

    # Funcion informe_materiales_prestados: realiza una parte del funcionamiento del programa
    def informe_materiales_prestados(self):
        resultado = []
        for m in self.materiales.values():
            if not m.esta_disponible():
                resultado.append(m)
        return resultado

    # Funcion informe_prestamos_vencidos: realiza una parte del funcionamiento del programa
    def informe_prestamos_vencidos(self):
        resultado = []
        for p in self.prestamos:
            if p.activo and p.esta_vencido():
                resultado.append(p)
        return resultado

    # Funcion informe_usuarios_sancionados: realiza una parte del funcionamiento del programa
    def informe_usuarios_sancionados(self):
        resultado = []
        for u in self.usuarios.values():
            if u.esta_sancionado():
                resultado.append(u)
        return resultado

    # Funcion informe_materiales_mas_usados: realiza una parte del funcionamiento del programa
    def informe_materiales_mas_usados(self):
        materiales = list(self.materiales.values())
        for i in range(len(materiales)):
            for j in range(i + 1, len(materiales)):
                usos_i = getattr(materiales[i], "_veces_prestado", 0)
                usos_j = getattr(materiales[j], "_veces_prestado", 0)
                if usos_i < usos_j:
                    materiales[i], materiales[j] = materiales[j], materiales[i]
        return materiales[:5]

    # GUARDAR

    # Funcion guardar_materiales: realiza una parte del funcionamiento del programa
    def guardar_materiales(self):
        data = []
        for m in self.materiales.values():
            data.append(m.to_dict())
        self.storage_materiales.guardar(data)

    # Funcion guardar_usuarios: realiza una parte del funcionamiento del programa
    def guardar_usuarios(self):
        data = []
        for u in self.usuarios.values():
            data.append(u.to_dict())
        self.storage_usuarios.guardar(data)

    # Funcion guardar_prestamos: realiza una parte del funcionamiento del programa
    def guardar_prestamos(self):
        data = []
        for p in self.prestamos:
            data.append(p.to_dict())
        self.storage_prestamos.guardar(data)

    # Funcion guardar_reservas: realiza una parte del funcionamiento del programa
    def guardar_reservas(self):
        data = []
        for r in self.reservas:
            data.append(r.to_dict())
        self.storage_reservas.guardar(data)

    # Funcion guardar_todo: realiza una parte del funcionamiento del programa
    def guardar_todo(self):
        self.guardar_materiales()
        self.guardar_usuarios()
        self.guardar_prestamos()
        self.guardar_reservas()

    # CARGAR

    # Funcion cargar_datos: realiza una parte del funcionamiento del programa
    def cargar_datos(self):
        self._cargar_materiales()
        self._cargar_usuarios()
        self._cargar_prestamos()
        self._cargar_reservas()

    # Funcion _cargar_materiales: realiza una parte del funcionamiento del programa
    def _cargar_materiales(self):
        data = self.storage_materiales.cargar()
        for m in data:
            tipo = m.get("tipo", "")
            if tipo == "libro":
                material = Libro(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("isbn", ""))
            elif tipo == "revista":
                material = Revista(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("numero_edicion", 0))
            elif tipo == "digital":
                material = RecursoDigital(m["id"], m["titulo"], m["autor"], m["categoria"], m.get("url", ""), m.get("formato", "ebook"))
            else:
                continue
            if not m.get("disponible", True):
                material.prestar()
            material._veces_prestado = m.get("veces_prestado", 0)
            self.materiales[m["id"]] = material

    # Funcion _cargar_usuarios: realiza una parte del funcionamiento del programa
    def _cargar_usuarios(self):
        data = self.storage_usuarios.cargar()

        for u in data:

            tipo = u.get("tipo", "usuario")
            telefono = u.get("telefono", "")

            if tipo == "socio":
                usuario = Socio(
                    u["id"],
                    u["nombre"],
                    telefono,
                    u.get("numero_socio", "")
                )

            elif tipo == "bibliotecario":
                usuario = Bibliotecario(
                    u["id"],
                    u["nombre"],
                    telefono,
                    u.get("numero_empleado", "")
                )

            elif tipo == "administrador":
                usuario = Administrador(
                    u["id"],
                    u["nombre"],
                    telefono
                )

            else:
                usuario = Usuario(
                    u["id"],
                    u["nombre"],
                    telefono
                )

            if u.get("sancionado", False):
                usuario.sancionar()

            usuario._prestamos_activos = u.get("prestamos_activos", 0)

            self.usuarios[u["id"]] = usuario

    # Funcion _cargar_prestamos: realiza una parte del funcionamiento del programa
    def _cargar_prestamos(self):
        from datetime import datetime
        data = self.storage_prestamos.cargar()
        for p in data:
            usuario = self.usuarios.get(p["usuario"])
            material = self.materiales.get(p["material"])
            if not usuario or not material:
                continue
            prestamo = Prestamo(usuario, material)
            prestamo.activo = p.get("activo", True)
            if "fecha_prestamo" in p:
                prestamo.fecha_prestamo = datetime.fromisoformat(p["fecha_prestamo"])
            if "fecha_vencimiento" in p:
                prestamo.fecha_vencimiento = datetime.fromisoformat(p["fecha_vencimiento"])
            if p.get("fecha_devolucion"):
                prestamo.fecha_devolucion = datetime.fromisoformat(p["fecha_devolucion"])
            self.prestamos.append(prestamo)

    # Funcion _cargar_reservas: realiza una parte del funcionamiento del programa
    def _cargar_reservas(self):
        from datetime import datetime
        data = self.storage_reservas.cargar()
        for r in data:
            u = self.usuarios.get(r["usuario"])
            m = self.materiales.get(r["material"])
            if not u or not m:
                continue
            reserva = Reserva(u, m)
            reserva.activa = r.get("activa", True)
            if "fecha_caducidad" in r:
                reserva.fecha_caducidad = datetime.fromisoformat(r["fecha_caducidad"])
            self.reservas.append(reserva)