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
        self.root.configure(bg="#0f172a")  # fondo oscuro futurista

        self.estilos()
        self.crear_layout()


    # =========================================================
    # 1.1 ESTILOS MODERNOS
    # =========================================================
    def estilos(self):
        style = ttk.Style()
        style.theme_use("default")

        # Treeview moderno oscuro
        style.configure(
            "Treeview",
            background="#111827",
            foreground="#e5e7eb",
            fieldbackground="#111827",
            rowheight=28,
            borderwidth=0,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#1f2937",
            foreground="white",
            font=("Segoe UI", 11, "bold")
        )

        style.map(
            "Treeview",
            background=[("selected", "#2563eb")],
            foreground=[("selected", "white")]
        )


    # =========================================================
    # 2. LAYOUT GENERAL
    # =========================================================
    def crear_layout(self):
        self.main_frame = tk.Frame(self.root, bg="#0f172a")
        self.main_frame.pack(fill="both", expand=True)

        # Sidebar futurista
        self.sidebar = tk.Frame(self.main_frame, bg="#0b1220", width=245)
        self.sidebar.pack(side="left", fill="y")

        self.sidebar.pack_propagate(False)

        # Contenido principal
        self.contenido = tk.Frame(self.main_frame, bg="#0f172a")
        self.contenido.pack(side="right", fill="both", expand=True)

        self.crear_sidebar()
        self.mostrar_inicio()


    def crear_sidebar(self):
        titulo = tk.Label(
            self.sidebar,
            text="📚 BIBLIOTECA",
            bg="#0b1220",
            fg="#38bdf8",
            font=("Segoe UI", 18, "bold")
        )
        titulo.pack(pady=25)

        self.crear_boton("📦 Materiales", self.mostrar_materiales)
        self.crear_boton("👤 Usuarios", self.mostrar_usuarios)
        self.crear_boton("🔄 Préstamos", self.mostrar_prestamos)
        self.crear_boton("📊 Informes", self.mostrar_informes)

        tk.Label(self.sidebar, bg="#0b1220").pack(expand=True)

        self.crear_boton("⛔ Salir", self.root.quit, color="#ef4444")


    def crear_boton(self, texto, comando, color="#1f2937"):
        btn = tk.Button(
            self.sidebar,
            text=texto,
            bg=color,
            fg="white",
            font=("Segoe UI", 11),
            relief="flat",
            activebackground="#2563eb",
            activeforeground="white",
            command=comando,
            padx=10,
            pady=12,
            cursor="hand2"
        )

        btn.pack(fill="x", padx=15, pady=6)

        # Hover effect
        def on_enter(e):
            btn.config(bg="#2563eb")

        def on_leave(e):
            btn.config(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)


    # =========================================================
    # 3. UTILIDADES
    # =========================================================
    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()


    def abrir_formulario(self, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.geometry("420x340")
        ventana.resizable(False, False)
        ventana.configure(bg="#0f172a")
        return ventana


    # =========================================================
    # 4. PANTALLAS PRINCIPALES
    # =========================================================
    def mostrar_inicio(self):
        self.limpiar_contenido()

        cont = tk.Frame(self.contenido, bg="#0f172a")
        cont.pack(expand=True)

        tk.Label(
            cont,
            text="Sistema de Biblioteca Inteligente",
            font=("Segoe UI", 26, "bold"),
            fg="#38bdf8",
            bg="#0f172a"
        ).pack(pady=20)

        tk.Label(
            cont,
            text="Gestión moderna de libros, usuarios y préstamos",
            font=("Segoe UI", 14),
            fg="#94a3b8",
            bg="#0f172a"
        ).pack()


    def mostrar_prestamos(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="🔄 Préstamos y Devoluciones",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)


    def mostrar_informes(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="📊 Informes",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)


    # =========================================================
    # 5. MÓDULO MATERIALES
    # =========================================================
    def mostrar_materiales(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="📦 Gestión de Materiales",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=15)

        frame_tabla = tk.Frame(self.contenido, bg="#0f172a")
        frame_tabla.pack(fill="both", expand=True, padx=25, pady=15)

        self.tabla_materiales = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Título", "Autor", "Categoría", "Disponible", "Tipo"),
            show="headings",
        )

        self.tabla_materiales.pack(fill="both", expand=True)

        cols = ("ID", "Título", "Autor", "Categoría", "Disponible", "Tipo")

        for col in cols:
            self.tabla_materiales.heading(col, text=col)

        self.tabla_materiales.column("ID", width=80, anchor="center")
        self.tabla_materiales.column("Título", width=240)
        self.tabla_materiales.column("Autor", width=160)
        self.tabla_materiales.column("Categoría", width=140)
        self.tabla_materiales.column("Disponible", width=110, anchor="center")
        self.tabla_materiales.column("Tipo", width=110, anchor="center")

        self.cargar_materiales()

        tk.Button(
            self.contenido,
            text="➕ Añadir libro",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
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
            tk.Label(
                win,
                text=campo,
                fg="white",
                bg="#0f172a",
                font=("Segoe UI", 10)
            ).pack(pady=3)

            entry = tk.Entry(
                win,
                bg="#1f2937",
                fg="white",
                insertbackground="white",
                relief="flat"
            )
            entry.pack(pady=3, ipady=4, ipadx=5)

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

        tk.Button(
            win,
            text="Guardar",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            command=guardar
        ).pack(pady=15)


    # =========================================================
    # 6. MÓDULO USUARIOS
    # =========================================================
    def mostrar_usuarios(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="👤 Gestión de Usuarios",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
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
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
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
            tk.Label(win, text=campo, fg="white", bg="#0f172a").pack(pady=3)

            entry = tk.Entry(
                win,
                bg="#1f2937",
                fg="white",
                insertbackground="white",
                relief="flat"
            )
            entry.pack(pady=3, ipady=4)

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

        tk.Button(
            win,
            text="Guardar",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            command=guardar
        ).pack(pady=15)