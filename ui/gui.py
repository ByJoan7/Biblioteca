import tkinter as tk
from tkinter import ttk


class BibliotecaApp:

    # =========================================================
    # 1. INICIALIZACIÓN
    # =========================================================
    def __init__(self, root, service):
        self.root = root
        self.service = service

        self.root.title("Sistema de Biblioteca")
        self.root.state("zoomed")

        self.crear_layout()


    # =========================================================
    # 2. LAYOUT GENERAL
    # =========================================================
    def crear_layout(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Sidebar
        self.sidebar = tk.Frame(self.main_frame, bg="#2c3e50", width=250)
        self.sidebar.pack(side="left", fill="y")

        # Contenido
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


    # =========================================================
    # 3. UTILIDADES
    # =========================================================
    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()


    def abrir_formulario(self, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("400x300")
        ventana.resizable(False, False)
        return ventana


    # =========================================================
    # 4. PANTALLAS PRINCIPALES
    # =========================================================
    def mostrar_inicio(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Bienvenido al Sistema de Biblioteca",
            font=("Arial", 24, "bold"),
            bg="#ecf0f1"
        ).pack(pady=50)


    def mostrar_prestamos(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Préstamos y Devoluciones",
            font=("Arial", 20),
            bg="#ecf0f1"
        ).pack(pady=20)


    def mostrar_informes(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Informes",
            font=("Arial", 20),
            bg="#ecf0f1"
        ).pack(pady=20)


    # =========================================================
    # 5. MÓDULO MATERIALES
    # =========================================================
    def mostrar_materiales(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Materiales",
            font=("Arial", 20),
            bg="#ecf0f1"
        ).pack(pady=20)

        frame_tabla = tk.Frame(self.contenido)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=20)

        scroll_y = tk.Scrollbar(frame_tabla, orient="vertical")
        scroll_x = tk.Scrollbar(frame_tabla, orient="horizontal")

        self.tabla_materiales = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Título", "Autor", "Categoría", "Disponible", "Tipo"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla_materiales.pack(fill="both", expand=True)

        # Cabeceras
        for col in ("ID", "Título", "Autor", "Categoría", "Disponible", "Tipo"):
            self.tabla_materiales.heading(col, text=col)

        # Columnas
        self.tabla_materiales.column("ID", width=80, anchor="center")
        self.tabla_materiales.column("Título", width=220)
        self.tabla_materiales.column("Autor", width=150)
        self.tabla_materiales.column("Categoría", width=130)
        self.tabla_materiales.column("Disponible", width=100, anchor="center")
        self.tabla_materiales.column("Tipo", width=100, anchor="center")

        self.cargar_materiales()

        tk.Button(
            self.contenido,
            text="➕ Añadir libro",
            bg="#27ae60",
            fg="white",
            command=self.formulario_nuevo_libro
        ).pack(pady=10)


    def cargar_materiales(self):
        for i in self.tabla_materiales.get_children():
            self.tabla_materiales.delete(i)

        for m in self.service.obtener_materiales():
            tipo = type(m).__name__

            self.tabla_materiales.insert(
                "",
                "end",
                values=(
                    m._id,
                    m._titulo,
                    m._autor,
                    m._categoria,
                    "Sí" if m.esta_disponible() else "No",
                    tipo
                )
            )


    def formulario_nuevo_libro(self):
        win = self.abrir_formulario("Nuevo Libro")

        entries = {}
        campos = ["ID", "Título", "Autor", "Categoría", "ISBN"]

        for campo in campos:
            tk.Label(win, text=campo).pack()
            entry = tk.Entry(win)
            entry.pack()
            entries[campo] = entry

        def guardar():
            from models.libro import Libro

            libro = Libro(
                entries["ID"].get(),
                entries["Título"].get(),
                entries["Autor"].get(),
                entries["Categoría"].get(),
                entries["ISBN"].get()
            )

            self.service.agregar_material(libro)
            self.cargar_materiales()
            win.destroy()

        tk.Button(win, text="Guardar", bg="#2ecc71", fg="white", command=guardar).pack(pady=10)


    # =========================================================
    # 6. MÓDULO USUARIOS
    # =========================================================
    def mostrar_usuarios(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Usuarios",
            font=("Arial", 20),
            bg="#ecf0f1"
        ).pack(pady=20)

        self.tabla_usuarios = ttk.Treeview(
            self.contenido,
            columns=("ID", "Nombre", "Tipo", "Sancionado"),
            show="headings"
        )

        for col in ("ID", "Nombre", "Tipo", "Sancionado"):
            self.tabla_usuarios.heading(col, text=col)

        self.tabla_usuarios.pack(fill="both", expand=True, padx=20, pady=20)

        self.cargar_usuarios()

        tk.Button(
            self.contenido,
            text="➕ Añadir usuario",
            bg="#2980b9",
            fg="white",
            command=self.formulario_usuario
        ).pack(pady=10)


    def cargar_usuarios(self):
        for i in self.tabla_usuarios.get_children():
            self.tabla_usuarios.delete(i)

        for u in self.service.obtener_usuarios():
            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    u._id,
                    u._nombre,
                    u._tipo,
                    "Sí" if u.esta_sancionado() else "No"
                )
            )


    def formulario_usuario(self):
        win = self.abrir_formulario("Nuevo Usuario")

        entries = {}
        campos = ["ID", "Nombre", "Tipo"]

        for campo in campos:
            tk.Label(win, text=campo).pack()
            entry = tk.Entry(win)
            entry.pack()
            entries[campo] = entry

        def guardar():
            from models.usuario import Usuario

            usuario = Usuario(
                entries["ID"].get(),
                entries["Nombre"].get(),
                entries["Tipo"].get()
            )

            self.service.agregar_usuario(usuario)
            self.cargar_usuarios()
            win.destroy()

        tk.Button(win, text="Guardar", bg="#2ecc71", fg="white", command=guardar).pack(pady=10)