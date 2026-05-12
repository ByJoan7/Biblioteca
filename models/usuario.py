class Usuario:
    def __init__(self, id, nombre):
        self._id = id
        self._nombre = nombre
        self._sancionado = False
        self._prestamos_activos = 0
        self._max_prestamos = 3

    def esta_sancionado(self):
        return self._sancionado

    def sancionar(self):
        self._sancionado = True

    def levantar_sancion(self):
        self._sancionado = False

    def puede_prestar(self):
        if self._sancionado:
            return False
        if self._prestamos_activos >= self._max_prestamos:
            return False
        return True

    def descripcion_corta(self):
        estado = "SANCIONADO" if self._sancionado else "Activo"
        return f"[{self._id}] {self._nombre} | {self.__class__.__name__} ({estado})"

    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "sancionado": self._sancionado,
            "prestamos_activos": self._prestamos_activos,
            "tipo": "usuario"
        }


class Socio(Usuario):
    def __init__(self, id, nombre, numero_socio):
        super().__init__(id, nombre)
        self._numero_socio = numero_socio
        self._max_prestamos = 3

    def to_dict(self):
        data = super().to_dict()
        data["numero_socio"] = self._numero_socio
        data["tipo"] = "socio"
        return data


class Bibliotecario(Usuario):
    def __init__(self, id, nombre, numero_empleado):
        super().__init__(id, nombre)
        self._numero_empleado = numero_empleado
        self._max_prestamos = 5

    def to_dict(self):
        data = super().to_dict()
        data["numero_empleado"] = self._numero_empleado
        data["tipo"] = "bibliotecario"
        return data


class Administrador(Usuario):
    def __init__(self, id, nombre):
        super().__init__(id, nombre)
        self._max_prestamos = 999

    def sancionar(self):
        pass

    def puede_prestar(self):
        return True

    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "administrador"
        return data
