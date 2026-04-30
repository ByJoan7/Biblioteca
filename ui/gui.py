import tkinter as tk
from tkinter import ttk


class BibliotecaApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Biblioteca")
        self.root.state("zoomed")

        self.crear_layout()

    def crear_layout(self):
        # ===== CONTENEDOR PRINCIPAL =====
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # ===== SIDEBAR =====
        self.sidebar = tk.Frame(self.main_frame, bg="#2c3e50", width=250)
        self.sidebar.pack(side="left", fill="y")

        # ===== CONTENIDO =====
        self.contenido = tk.Frame(self.main_frame, bg="#ecf0f1")
        self.contenido.pack(side="right", fill="both", expand=True)

        self.crear_sidebar()
        self.mostrar_inicio()

    def crear_sidebar(self):
        titulo = tk.Label(
            self.sidebar,
            text="Biblioteca",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=20)

        # Botones menú
        self.crear_boton("Materiales", self.mostrar_materiales)
        self.crear_boton("Usuarios", self.mostrar_usuarios)
        self.crear_boton("Préstamos", self.mostrar_prestamos)
        self.crear_boton("Informes", self.mostrar_informes)

        tk.Label(self.sidebar, bg="#2c3e50").pack(expand=True)

        self.crear_boton("Salir", self.root.quit, color="#e74c3c")

    def crear_boton(self, texto, comando, color="#34495e"):
        btn = tk.Button(
            self.sidebar,
            text=texto,
            bg=color,
            fg="white",
            font=("Arial", 12),
            relief="flat",
            command=comando,
            padx=10,
            pady=10
        )
        btn.pack(fill="x", padx=10, pady=5)

    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # ===== PANTALLAS =====

    def mostrar_inicio(self):
        self.limpiar_contenido()

        label = tk.Label(
            self.contenido,
            text="Bienvenido al Sistema de Biblioteca",
            font=("Arial", 24, "bold"),
            bg="#ecf0f1"
        )
        label.pack(pady=50)

    def mostrar_materiales(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Gestión de Materiales", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)

        # TABLA
        tabla = ttk.Treeview(self.contenido, columns=("ID", "Título"), show="headings")
        tabla.heading("ID", text="ID")
        tabla.heading("Título", text="Título")
        tabla.pack(pady=20, fill="x", padx=20)

        # BOTÓN
        btn = tk.Button(self.contenido, text="Añadir libro", bg="#27ae60", fg="white")
        btn.pack(pady=10)

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Gestión de Usuarios", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)

    def mostrar_prestamos(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Préstamos y Devoluciones", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)

    def mostrar_informes(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Informes", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)