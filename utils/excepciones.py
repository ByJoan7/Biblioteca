class BibliotecaError(Exception):
    pass

class UsuarioSancionadoError(BibliotecaError):
    pass

class MaterialNoDisponibleError(BibliotecaError):
    pass