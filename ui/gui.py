import tkinter as tk
from tkinter import ttk


class BibliotecaApp:

    def __init__(self, root, service):
        self.root = root
        self.service = service
        
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

        titulo = tk.Label(
            self.contenido,
            text="Gestión de Materiales",
            font=("Arial", 20),
            bg="#ecf0f1"
        )
        titulo.pack(pady=20)

        # ===== CONTENEDOR TABLA =====
        frame_tabla = tk.Frame(self.contenido)
        frame_tabla.pack(fill="both", expand=True, padx=20, pady=20)

        # ===== SCROLLBARS =====
        scroll_y = tk.Scrollbar(frame_tabla, orient="vertical")
        scroll_x = tk.Scrollbar(frame_tabla, orient="horizontal")

        # ===== TABLA =====
        self.tabla_materiales = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Título", "Autor", "Categoría", "Disponible", "Tipo"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        self.tabla_materiales.pack(fill="both", expand=True)

        # ===== CABECERAS =====
        self.tabla_materiales.heading("ID", text="ID")
        self.tabla_materiales.heading("Título", text="Título")
        self.tabla_materiales.heading("Autor", text="Autor")
        self.tabla_materiales.heading("Categoría", text="Categoría")
        self.tabla_materiales.heading("Disponible", text="Disponible")
        self.tabla_materiales.heading("Tipo", text="Tipo")

        # ===== ANCHO DE COLUMNAS =====
        self.tabla_materiales.column("ID", width=80, anchor="center")
        self.tabla_materiales.column("Título", width=220)
        self.tabla_materiales.column("Autor", width=150)
        self.tabla_materiales.column("Categoría", width=130)
        self.tabla_materiales.column("Disponible", width=100, anchor="center")
        self.tabla_materiales.column("Tipo", width=100, anchor="center")

        # ===== CARGAR DATOS =====
        self.cargar_materiales()

        # ===== BOTÓN AÑADIR =====
        tk.Button(
            self.contenido,
            text="➕ Añadir libro",
            bg="#27ae60",
            fg="white",
            font=("Arial", 12),
            command=self.formulario_nuevo_libro
        ).pack(pady=10)

    def mostrar_usuarios(self):
        self.limpiar_contenido()

        titulo = tk.Label(
            self.contenido,
            text="Gestión de Usuarios",
            font=("Arial", 20),
            bg="#ecf0f1"
        )
        titulo.pack(pady=20)

        self.tabla_usuarios = ttk.Treeview(
            self.contenido,
            columns=("ID", "Nombre", "Tipo", "Sancionado"),
            show="headings"
        )

        self.tabla_usuarios.heading("ID", text="ID")
        self.tabla_usuarios.heading("Nombre", text="Nombre")
        self.tabla_usuarios.heading("Tipo", text="Tipo")
        self.tabla_usuarios.heading("Sancionado", text="Sancionado")

        self.tabla_usuarios.pack(fill="both", expand=True, padx=20, pady=20)

        self.cargar_usuarios()

        tk.Button(
            self.contenido,
            text="➕ Añadir usuario",
            bg="#2980b9",
            fg="white",
            command=self.formulario_usuario
        ).pack(pady=10)

    def mostrar_prestamos(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Préstamos y Devoluciones", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)

    def mostrar_informes(self):
        self.limpiar_contenido()

        titulo = tk.Label(self.contenido, text="Informes", font=("Arial", 20), bg="#ecf0f1")
        titulo.pack(pady=20)

    def abrir_formulario(self, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("400x300")
        ventana.resizable(False, False)
        return ventana
    
    def cargar_materiales(self):
        for i in self.tabla_materiales.get_children():
            self.tabla_materiales.delete(i)

        for m in self.service.obtener_materiales():

            tipo = getattr(m, "__class__", type(m)).__name__

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

        tk.Label(win, text="ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Label(win, text="Título").pack()
        titulo_entry = tk.Entry(win)
        titulo_entry.pack()

        tk.Label(win, text="Autor").pack()
        autor_entry = tk.Entry(win)
        autor_entry.pack()

        tk.Label(win, text="Categoría").pack()
        cat_entry = tk.Entry(win)
        cat_entry.pack()

        tk.Label(win, text="ISBN").pack()
        isbn_entry = tk.Entry(win)
        isbn_entry.pack()

        def guardar():
            from models.libro import Libro

            libro = Libro(
                id_entry.get(),
                titulo_entry.get(),
                autor_entry.get(),
                cat_entry.get(),
                isbn_entry.get()
            )

            self.service.agregar_material(libro)
            self.cargar_materiales()
            win.destroy()

        tk.Button(
            win,
            text="Guardar",
            bg="#2ecc71",
            fg="white",
            command=guardar
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

        tk.Label(win, text="ID").pack()
        id_entry = tk.Entry(win)
        id_entry.pack()

        tk.Label(win, text="Nombre").pack()
        nombre_entry = tk.Entry(win)
        nombre_entry.pack()

        tk.Label(win, text="Tipo (socio/admin/bibliotecario)").pack()
        tipo_entry = tk.Entry(win)
        tipo_entry.pack()

        def guardar():
            from models.usuario import Usuario

            usuario = Usuario(
                id_entry.get(),
                nombre_entry.get(),
                tipo_entry.get()
            )

            self.service.agregar_usuario(usuario)
            self.cargar_usuarios()
            win.destroy()

        tk.Button(
            win,
            text="Guardar",
            bg="#2ecc71",
            fg="white",
            command=guardar
        ).pack(pady=10)
    
