# Archivo: main.py
# Este archivo forma parte del sistema de biblioteca.
import tkinter as tk
from ui.gui import BibliotecaApp
from services.biblioteca_service import BibliotecaService

# Funcion main: realiza una parte del funcionamiento del programa
def main():
    root = tk.Tk()

    # Servicio principal (carga datos desde JSON automáticamente)
    service = BibliotecaService()

    # Interfaz gráfica
    app = BibliotecaApp(root, service)

    root.mainloop()

if __name__ == "__main__":
    main()