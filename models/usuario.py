# Archivo: usuario.py
# Este archivo forma parte del sistema de biblioteca.

# Esta clase representa Usuario
class Usuario:
    # Constructor de la clase

    def __init__(self, id, nombre, telefono):
        self._id = id
        self._nombre = nombre
        self._telefono = telefono
        self._sancionado = False
        self._prestamos_activos = 0
        self._max_prestamos = 3

    # Funcion esta_sancionado: realiza una parte del funcionamiento del programa
    def esta_sancionado(self):
        return self._sancionado

    # Funcion sancionar: realiza una parte del funcionamiento del programa
    def sancionar(self):
        self._sancionado = True

    # Funcion levantar_sancion: realiza una parte del funcionamiento del programa
    def levantar_sancion(self):
        self._sancionado = False

    # Funcion puede_prestar: realiza una parte del funcionamiento del programa
    def puede_prestar(self):
        if self._sancionado:
            return False
        if self._prestamos_activos >= self._max_prestamos:
            return False
        return True

    # Funcion descripcion_corta: realiza una parte del funcionamiento del programa
    def descripcion_corta(self):
        estado = "SANCIONADO" if self._sancionado else "Activo"
        return f"[{self._id}] {self._nombre} | {self.__class__.__name__} ({estado})"

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        return {
            "id": self._id,
            "nombre": self._nombre,
            "telefono": self._telefono,
            "sancionado": self._sancionado,
            "prestamos_activos": self._prestamos_activos,
            "tipo": "usuario"
        }



# Esta clase representa Socio
class Socio(Usuario):
    # Constructor de la clase

    def __init__(self, id, nombre, telefono, numero_socio):
        super().__init__(id, nombre, telefono)
        self._numero_socio = numero_socio
        self._max_prestamos = 3

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        data = super().to_dict()
        data["numero_socio"] = self._numero_socio
        data["tipo"] = "socio"
        return data



# Esta clase representa Bibliotecario
class Bibliotecario(Usuario):
    # Constructor de la clase

    def __init__(self, id, nombre, telefono, numero_empleado):
        super().__init__(id, nombre, telefono)
        self._numero_empleado = numero_empleado
        self._max_prestamos = 5

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        data = super().to_dict()
        data["numero_empleado"] = self._numero_empleado
        data["tipo"] = "bibliotecario"
        return data



# Esta clase representa Administrador
class Administrador(Usuario):
    # Constructor de la clase

    def __init__(self, id, nombre, telefono):
        super().__init__(id, nombre, telefono)
        self._max_prestamos = 999

    # Funcion sancionar: realiza una parte del funcionamiento del programa
    def sancionar(self):
        pass

    # Funcion puede_prestar: realiza una parte del funcionamiento del programa
    def puede_prestar(self):
        return True

    # Funcion to_dict: realiza una parte del funcionamiento del programa
    def to_dict(self):
        data = super().to_dict()
        data["tipo"] = "administrador"
        return data