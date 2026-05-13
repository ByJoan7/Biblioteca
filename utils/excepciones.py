# Archivo: excepciones.py
# Este archivo forma parte del sistema de biblioteca.

# Esta clase representa BibliotecaError
class BibliotecaError(Exception):
    pass


# Esta clase representa UsuarioSancionadoError
class UsuarioSancionadoError(BibliotecaError):
    pass


# Esta clase representa MaterialNoDisponibleError
class MaterialNoDisponibleError(BibliotecaError):
    pass