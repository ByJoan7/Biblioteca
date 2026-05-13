# Archivo: gui.py
# Este archivo forma parte del sistema de biblioteca.
import tkinter as tk
from tkinter import ttk
import random



# Esta clase representa BibliotecaApp
class BibliotecaApp:

    # =========================================================
    # 1. INICIALIZACIÓN
    # =========================================================

    # Constructor de la clase

    def __init__(self, root, service):
        self.root = root
        self.service = service

        self.root.title("Sistema de Biblioteca")
        self.root.state("zoomed")
        self.root.configure(bg="#0f172a")  # fondo oscuro futurista

        self.estilos()
        self.crear_layout()

    # =========================================================
    # 1.1 ESTILOS 
    # =========================================================

    # Funcion estilos: realiza una parte del funcionamiento del programa
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

    # Funcion crear_layout: realiza una parte del funcionamiento del programa
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

    # Funcion crear_sidebar: realiza una parte del funcionamiento del programa
    def crear_sidebar(self):
        titulo = tk.Label(
            self.sidebar,
            text="📚 BIBLIOTECA",
            bg="#0b1220",
            fg="#38bdf8",
            font=("Segoe UI", 18, "bold")
        )
        titulo.pack(pady=25)

        self.crear_boton("👤 Usuarios", self.mostrar_usuarios)
        self.crear_boton("📦 Materiales", self.mostrar_materiales)
        self.crear_boton("🔄 Préstamos", self.mostrar_prestamos)
        self.crear_boton("📅 Reservas", self.mostrar_reservas)
        self.crear_boton("📊 Informes", self.mostrar_informes)

        tk.Label(self.sidebar, bg="#0b1220").pack(expand=True)

        self.crear_boton("⛔ Salir", self.root.quit, color="#ef4444")

    # Funcion crear_boton: realiza una parte del funcionamiento del programa
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
        # Funcion on_enter: realiza una parte del funcionamiento del programa
        def on_enter(e):
            btn.config(bg="#2563eb")

        # Funcion on_leave: realiza una parte del funcionamiento del programa
        def on_leave(e):
            btn.config(bg=color)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

    # =========================================================
    # 3. UTILIDADES
    # =========================================================

    # Funcion limpiar_contenido: realiza una parte del funcionamiento del programa
    def limpiar_contenido(self):
        for widget in self.contenido.winfo_children():
            widget.destroy()

    # Funcion abrir_formulario: realiza una parte del funcionamiento del programa
    def abrir_formulario(self, titulo, ancho=420, alto=340):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        ventana.resizable(False, False)
        ventana.configure(bg="#0f172a")

        ventana.update_idletasks()

        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        ventana.geometry(f"{ancho}x{alto}+{x}+{y}")
        ventana.deiconify()
        
        return ventana

    # Funcion crear_scrollable_frame: realiza una parte del funcionamiento del programa
    def crear_scrollable_frame(self, parent):
        canvas = tk.Canvas(parent, bg="#0f172a", highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#0f172a")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        # Ajustar ancho del frame al canvas
        # Funcion on_canvas_configure: realiza una parte del funcionamiento del programa
        def on_canvas_configure(e):
            canvas.itemconfig(window_id, width=e.width)

        window_id = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.bind("<Configure>", on_canvas_configure)
        
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        return scrollable_frame

    # =========================================================
    # 4. PANTALLAS PRINCIPALES
    # =========================================================

    # Funcion mostrar_inicio: realiza una parte del funcionamiento del programa
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

    # Funcion mostrar_prestamos: realiza una parte del funcionamiento del programa
    def mostrar_prestamos(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="🔄 Préstamos y Devoluciones",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)

        frame_tabla = tk.Frame(self.contenido, bg="#0f172a")
        frame_tabla.pack(fill="both", expand=True, padx=25, pady=15)

        self.tabla_prestamos = ttk.Treeview(
            frame_tabla,
            columns=("Usuario", "Material", "Vencimiento", "Estado", "Multa"),
            show="headings",
        )
        self.tabla_prestamos.pack(fill="both", expand=True)

        for col in ("Usuario", "Material", "Vencimiento", "Estado", "Multa"):
            self.tabla_prestamos.heading(col, text=col)

        self.cargar_prestamos()

        frame_acciones = tk.Frame(self.contenido, bg="#0f172a")
        frame_acciones.pack(pady=10)

        tk.Button(
            frame_acciones,
            text="🤝 Prestar",
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.formulario_prestar
        ).pack(side="left", padx=10)

        tk.Button(
            frame_acciones,
            text="🔙 Devolver",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.devolver_seleccionado
        ).pack(side="left", padx=10)

    # Funcion centrar_ventana: realiza una parte del funcionamiento del programa
    def centrar_ventana(self, win, ancho, alto):
        win.update_idletasks()

        pantalla_ancho = win.winfo_screenwidth()
        pantalla_alto = win.winfo_screenheight()

        x = (pantalla_ancho // 2) - (ancho // 2)
        y = (pantalla_alto // 2) - (alto // 2)

        win.geometry(f"{ancho}x{alto}+{x}+{y}")

    # =========================================================
    # 6. MÓDULO USUARIOS
    # =========================================================

    # Funcion mostrar_usuarios: realiza una parte del funcionamiento del programa
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
            columns=("ID", "Nombre", "Sancionado"),
            show="headings"
        )

        for col in ("ID", "Nombre", "Sancionado"):
            self.tabla_usuarios.heading(col, text=col)

        self.tabla_usuarios.pack(fill="both", expand=True, padx=20, pady=20)

        self.cargar_usuarios()

        frame_acciones = tk.Frame(self.contenido, bg="#0f172a")
        frame_acciones.pack(pady=10)

        tk.Button(
            frame_acciones,
            text="➕ Añadir",
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.formulario_usuario
        ).pack(side="left", padx=10)

        tk.Button(
            frame_acciones,
            text="✏️ Editar",
            bg="#f59e0b",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.formulario_editar_usuario
        ).pack(side="left", padx=10)

        tk.Button(
            frame_acciones,
            text="🗑️ Eliminar",
            bg="#ef4444",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.eliminar_usuario_seleccionado
        ).pack(side="left", padx=10)

    # Funcion cargar_usuarios: realiza una parte del funcionamiento del programa
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
                    "Sí" if u.esta_sancionado() else "No"
                )
            )

    # Funcion generar_id_usuario: realiza una parte del funcionamiento del programa
    def generar_id_usuario(self):
        ids_existentes = {
            str(usuario._id)
            for usuario in self.service.obtener_usuarios()
        }
        while True:
            nuevo_id = str(random.randint(1, 9999))

            if nuevo_id not in ids_existentes:
                return nuevo_id

    # Funcion formulario_usuario: realiza una parte del funcionamiento del programa
    def formulario_usuario(self):
        win = self.abrir_formulario("Nuevo Usuario")
        win.configure(bg="#0f172a")

        win.resizable(True, True)
        container = tk.Frame(win, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=10, pady=10)
        main = self.crear_scrollable_frame(container)

        entries = {}
        campos = ["Nombre"]

        for campo in campos:
            tk.Label(
                main,
                text=campo,
                fg="white",
                bg="#0f172a",
                font=("Segoe UI", 10)
            ).pack(anchor="w", pady=(8, 2))

            entry = tk.Entry(
                main,
                bg="#1f2937",
                fg="white",
                insertbackground="white",
                relief="flat"
            )
            entry.pack(fill="x", ipady=6)

            entries[campo] = entry

        # Esta funcion guarda datos

        def guardar():
            from models.usuario import Usuario

            nuevo_id = self.generar_id_usuario()

            usuario = Usuario(
                nuevo_id,
                entries["Nombre"].get()
            )

            self.service.agregar_usuario(usuario)
            self.cargar_usuarios()
            win.destroy()

        tk.Frame(main, height=10, bg="#0f172a").pack()

        btn = tk.Button(
            main,
            text="Guardar",
            bg="#22c55e",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            command=guardar,
            cursor="hand2"
        )
        btn.pack(fill="x", pady=(15, 0))

    # Funcion eliminar_usuario_seleccionado: realiza una parte del funcionamiento del programa
    def eliminar_usuario_seleccionado(self):
        item = self.tabla_usuarios.selection()
        if not item:
            return
        u_id = self.tabla_usuarios.item(item)["values"][0]
        if self.service.eliminar_usuario(str(u_id)):
            self.cargar_usuarios()

    # Funcion formulario_editar_usuario: realiza una parte del funcionamiento del programa
    def formulario_editar_usuario(self):
        item = self.tabla_usuarios.selection()
        if not item:
            return
        valores = self.tabla_usuarios.item(item)["values"]
        u_id = str(valores[0])

        win = self.abrir_formulario("Editar Usuario", alto=200)
        main = self.crear_scrollable_frame(win)
        
        tk.Label(main, text="Nombre", fg="white", bg="#0f172a").pack(anchor="w")
        name_entry = tk.Entry(main, bg="#1f2937", fg="white")
        name_entry.insert(0, valores[1])
        name_entry.pack(fill="x", ipady=6)

        # Esta funcion guarda datos

        def guardar():
            self.service.modificar_usuario(u_id, {"nombre": name_entry.get()})
            self.cargar_usuarios()
            win.destroy()

        tk.Button(main, text="Guardar", bg="#f59e0b", fg="white", command=guardar).pack(fill="x", pady=20)

    # =========================================================
    # 5. MÓDULO MATERIALES
    # =========================================================

    # Funcion mostrar_materiales: realiza una parte del funcionamiento del programa
    def mostrar_materiales(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="👤 Gestión de Materiales",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)

        cont = self.crear_scrollable_frame(self.contenido)

        self.crear_seccion_material(cont, "📚 Libros", "libro")
        self.crear_seccion_material(cont, "💻 Recursos Digitales", "digital")
        self.crear_seccion_material(cont, "📰 Revistas", "revista")

    # Funcion crear_seccion_material: realiza una parte del funcionamiento del programa
    def crear_seccion_material(self, parent, titulo, tipo):
        frame = tk.Frame(parent, bg="#1e293b")
        frame.pack(fill="x", padx=20, pady=10)

        # Título
        tk.Label(
            frame,
            text=titulo,
            font=("Segoe UI", 14, "bold"),
            fg="#38bdf8",
            bg="#1e293b"
        ).pack(anchor="w", padx=10, pady=(8, 4))

        # Barra superior (buscador + botones en la misma línea)
        top = tk.Frame(frame, bg="#1e293b")
        top.pack(fill="x", padx=10, pady=(0, 5))

        entry = tk.Entry(top, bg="#111827", fg="white", relief="flat")
        entry.pack(side="left", fill="x", expand=True, ipady=4)

        # Botones a la derecha (más compacto)
        btn_frame = tk.Frame(top, bg="#1e293b")
        btn_frame.pack(side="right")

        # Funcion btn: realiza una parte del funcionamiento del programa
        def btn(txt, color):
            return tk.Button(
                btn_frame,
                text=txt,
                bg=color,
                fg="white",
                font=("Segoe UI", 9, "bold"),
                relief="flat",
                padx=6,
                pady=3,
                cursor="hand2"
            )

        # Funcion accion_add: realiza una parte del funcionamiento del programa
        def accion_add():
            if tipo == "libro":
                self.formulario_nuevo_libro("Libro")
            elif tipo == "digital":
                self.formulario_nuevo_libro("Digital")
            elif tipo == "revista":
                self.formulario_nuevo_libro("Revista")

        tk.Button(
            btn_frame,
            text="➕",
            bg="#22c55e",
            fg="white",
            command=accion_add,
            font=("Segoe UI", 9, "bold"),
            relief="flat",
            padx=6,
            pady=3,
            cursor="hand2"
        ).pack(side="left", padx=2)
        btn_edit = btn("✏️", "#f59e0b")
        btn_edit.pack(side="left", padx=2)
        btn_delete = btn("🗑️", "#ef4444")
        btn_delete.pack(side="left", padx=2)

        # Columnas según tipo
        if tipo == "libro":
            columnas = ("ID", "Título", "Autor", "Categoría", "ISBN", "Disp")
        elif tipo == "digital":
            columnas = ("ID", "Título", "Autor", "Categoría", "URL", "Disp")
        elif tipo == "revista":
            columnas = ("ID", "Título", "Autor", "Categoría", "Edición", "Disp")

        tabla = ttk.Treeview(
            frame,
            columns=columnas,
            show="headings",
            height=5
        )

        for col in columnas:
            tabla.heading(col, text=col)

        tabla.heading("ID", text="ID")
        tabla.heading("Título", text="Título")
        tabla.heading("Autor", text="Autor")
        tabla.heading("Categoría", text="Categoría")
        tabla.heading("Disp", text="✔")

        tabla.column("ID", width=60, anchor="center")
        tabla.column("Título", width=180)
        tabla.column("Autor", width=120)
        tabla.column("Categoría", width=100)

        if tipo == "libro":
            tabla.column("ISBN", width=120)
        elif tipo == "digital":
            tabla.column("URL", width=180)
        elif tipo == "revista":
            tabla.column("Edición", width=80)

        tabla.column("Disp", width=50, anchor="center")

        tabla.pack(fill="x", padx=10, pady=(0, 10))

        # Funcion accion_delete: realiza una parte del funcionamiento del programa
        def accion_delete():
            item = tabla.selection()
            if not item:
                return
            m_id = str(tabla.item(item)["values"][0])
            if self.service.eliminar_material(m_id):
                cargar(entry.get())

        # Funcion accion_edit: realiza una parte del funcionamiento del programa
        def accion_edit():
            item = tabla.selection()
            if not item:
                return
            valores = tabla.item(item)["values"]
            self.formulario_editar_material_seccion(valores, tipo, lambda: cargar(entry.get()))

        btn_delete.config(command=accion_delete)
        btn_edit.config(command=accion_edit)

        # Cargar datos
        # Esta funcion carga datos

        def cargar(filtro=""):
            for i in tabla.get_children():
                tabla.delete(i)

            for m in self.service.obtener_materiales():
                if m.to_dict()["tipo"] != tipo:
                    continue

                if filtro and filtro.lower() not in m._titulo.lower():
                    continue

                # Obtener atributo extra según tipo
                if tipo == "libro":
                    extra = getattr(m, "_isbn", "")
                elif tipo == "digital":
                    extra = getattr(m, "_url", "")
                elif tipo == "revista":
                    extra = getattr(m, "_numero_edicion", "")

                tabla.insert(
                    "",
                    "end",
                    values=(
                        m._id,
                        m._titulo,
                        m._autor,
                        m._categoria,
                        extra,
                        "✔" if m.esta_disponible() else "✖"
                    )
                )

        entry.bind("<KeyRelease>", lambda e: cargar(entry.get()))
        cargar()

    # Funcion cargar_materiales: realiza una parte del funcionamiento del programa
    def cargar_materiales(self, filtro=""):
        for i in self.tabla_materiales.get_children():
            self.tabla_materiales.delete(i)

        if filtro:
            materiales = self.service.buscar_materiales(self.criterio_busqueda.get(), filtro)
        else:
            materiales = self.service.obtener_materiales()

        for m in materiales:
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

    # Funcion generar_id_material: realiza una parte del funcionamiento del programa
    def generar_id_material(self):
        ids_existentes = {
            str(material._id)
            for material in self.service.obtener_materiales()
        }

        while True:
            nuevo_id = str(random.randint(1, 9999))

            if nuevo_id not in ids_existentes:
                return nuevo_id

    # Funcion formulario_nuevo_libro: realiza una parte del funcionamiento del programa
    def formulario_nuevo_libro(self, tipo_preseleccionado="Libro"):
        win = self.abrir_formulario("Nuevo Material")
        win.configure(bg="#0f172a")

        container = tk.Frame(win, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=10, pady=10)

        main = self.crear_scrollable_frame(container)

        # Tipo
        tk.Label(main, text="Tipo de Material", fg="white", bg="#0f172a").pack(anchor="w")
        var_tipo = tk.StringVar(value=tipo_preseleccionado)

        tipo_cb = ttk.Combobox(
            main,
            textvariable=var_tipo,
            values=["Libro", "Revista", "Digital"],
            state="readonly"
        )
        tipo_cb.pack(fill="x", ipady=4, pady=(0, 10))

        entries = {}
        campos = ["Título", "Autor", "Categoría", "ISBN / URL / Edición"]

        for campo in campos:
            tk.Label(main, text=campo, fg="white", bg="#0f172a").pack(anchor="w", pady=(8, 2))
            entry = tk.Entry(main, bg="#1f2937", fg="white", relief="flat")
            entry.pack(fill="x", ipady=6)
            entries[campo] = entry

        # Esta funcion guarda datos

        def guardar():
            from models.libro import Libro
            from models.revista import Revista
            from models.recurso_digital import RecursoDigital

            t = var_tipo.get()
            id_val = self.generar_id_material()
            tit = entries["Título"].get()
            aut = entries["Autor"].get()
            cat = entries["Categoría"].get()
            extra = entries["ISBN / URL / Edición"].get()

            if t == "Libro":
                material = Libro(id_val, tit, aut, cat, extra)
            elif t == "Revista":
                material = Revista(id_val, tit, aut, cat, extra)
            else:
                material = RecursoDigital(id_val, tit, aut, cat, extra)

            self.service.agregar_material(material)
            self.mostrar_materiales()  
            win.destroy()

        tk.Button(
            main,
            text="Guardar",
            bg="#22c55e",
            fg="white",
            command=guardar
        ).pack(fill="x", pady=15)

    # Funcion formulario_editar_material_seccion: realiza una parte del funcionamiento del programa
    def formulario_editar_material_seccion(self, valores, tipo, callback_cargar):
        material_id = str(valores[0])
        
        win = self.abrir_formulario(f"Editar {tipo.capitalize()}")
        win.resizable(True, True)
        
        container = tk.Frame(win, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=10, pady=10)
        
        main = self.crear_scrollable_frame(container)

        entries = {}
        campos = ["Título", "Autor", "Categoría"]
        actuales = {"Título": valores[1], "Autor": valores[2], "Categoría": valores[3]}
        
        if tipo == "libro":
            campos.append("ISBN")
            actuales["ISBN"] = valores[4]
        elif tipo == "digital":
            campos.append("URL")
            actuales["URL"] = valores[4]
        elif tipo == "revista":
            campos.append("Edición")
            actuales["Edición"] = valores[4]

        for campo in campos:
            tk.Label(main, text=campo, fg="white", bg="#0f172a").pack(anchor="w", pady=(8, 2))
            entry = tk.Entry(main, bg="#1f2937", fg="white", relief="flat")
            entry.insert(0, actuales[campo])
            entry.pack(fill="x", ipady=6)
            entries[campo] = entry

        # Esta funcion guarda datos

        def guardar():
            datos = {
                "titulo": entries["Título"].get(),
                "autor": entries["Autor"].get(),
                "categoria": entries["Categoría"].get()
            }
            if "ISBN" in entries:
                datos["isbn"] = entries["ISBN"].get()
            if "URL" in entries:
                datos["url"] = entries["URL"].get()
            if "Edición" in entries:
                try:
                    datos["numero_edicion"] = int(entries["Edición"].get())
                except ValueError:
                    datos["numero_edicion"] = entries["Edición"].get()
                
            self.service.modificar_material(material_id, datos)
            callback_cargar()
            win.destroy()

        tk.Button(main, text="Guardar Cambios", bg="#f59e0b", fg="white", command=guardar).pack(fill="x", pady=20)

    # =========================================================
    # 6. MÓDULO PRESTAMOS Y DEVOLUCIONES
    # =========================================================

    # Funcion cargar_prestamos: realiza una parte del funcionamiento del programa
    def cargar_prestamos(self):
        for i in self.tabla_prestamos.get_children():
            self.tabla_prestamos.delete(i)

        for p in self.service.prestamos:
            estado = "Activo" if p.activo else "Devuelto"
            if p.activo and p.esta_vencido():
                estado = "VENCIDO"
            
            multa = f"{p.calcular_multa():.2f}€"
            
            self.tabla_prestamos.insert(
                "",
                "end",
                values=(
                    p.usuario._nombre,
                    p.material._titulo,
                    p.fecha_vencimiento.strftime("%d/%m/%Y"),
                    estado,
                    multa
                )
            )

    # Funcion formulario_prestar: realiza una parte del funcionamiento del programa
    def formulario_prestar(self):
        win = self.abrir_formulario("Realizar Préstamo", alto=400)

        container = tk.Frame(win, bg="#0f172a")
        container.pack(fill="both", expand=True, padx=20, pady=20)

        main = self.crear_scrollable_frame(container)

        # Desplegable donde ver los usuarios a los que poder prestar

        tk.Label(
            main,
            text="Usuario",
            fg="white",
            bg="#0f172a"
        ).pack(anchor="w")

        usuarios = self.service.obtener_usuarios()

        usuarios_dict = {
            f"{u._id} - {u._nombre}": u._id
            for u in usuarios
        }

        usuario_var = tk.StringVar()

        usuario_combo = ttk.Combobox(
            main,
            textvariable=usuario_var,
            values=list(usuarios_dict.keys()),
            state="readonly"
        )

        usuario_combo.pack(fill="x", ipady=5)

        # Desplegable donde ver los libros que se pueden prestar

        tk.Label(
            main,
            text="Material",
            fg="white",
            bg="#0f172a"
        ).pack(anchor="w", pady=(15, 0))

        materiales = [
            m for m in self.service.obtener_materiales()
            if m.esta_disponible()
        ]

        materiales_dict = {}

        for m in materiales:

            # Libro
            if hasattr(m, "_isbn"):
                texto = f"{m._id} - ISBN: {m._isbn}"

            # Revista
            elif hasattr(m, "_numero_edicion"):
                texto = f"{m._id} - Edición: {m._numero_edicion}"

            # Digital
            elif hasattr(m, "_url"):
                texto = f"{m._id} - URL"

            else:
                texto = f"{m._id}"

            materiales_dict[texto] = m._id

        material_var = tk.StringVar()

        material_combo = ttk.Combobox(
            main,
            textvariable=material_var,
            values=list(materiales_dict.keys()),
            state="readonly"
        )

        material_combo.pack(fill="x", ipady=5)

        # Días que se presta el libro

        tk.Label(
            main,
            text="Días de préstamo",
            fg="white",
            bg="#0f172a"
        ).pack(anchor="w", pady=(15, 0))

        dias = tk.Entry(
            main,
            bg="#1f2937",
            fg="white"
        )

        dias.insert(0, "14")
        dias.pack(fill="x", ipady=6)

        # =========================
        # PRESTAR
        # =========================

        # Funcion realizar: realiza una parte del funcionamiento del programa
        def realizar():
            try:

                usuario_texto = usuario_var.get()
                material_texto = material_var.get()

                if not usuario_texto:
                    raise Exception("Selecciona un usuario")

                if not material_texto:
                    raise Exception("Selecciona un material")

                usuario_id = usuarios_dict[usuario_texto]
                material_id = materiales_dict[material_texto]

                self.service.prestar_material(
                    str(usuario_id),
                    str(material_id),
                    int(dias.get())
                )

                self.cargar_prestamos()
                self.mostrar_materiales()

                win.destroy()

            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", str(e))

        tk.Button(
            main,
            text="Prestar",
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=realizar
        ).pack(fill="x", pady=20)

    # Funcion devolver_seleccionado: realiza una parte del funcionamiento del programa
    def devolver_seleccionado(self):
        item = self.tabla_prestamos.selection()
        if not item:
            return
        
        # Encontrar el préstamo correspondiente
        idx = self.tabla_prestamos.index(item)
        prestamo = self.service.prestamos[idx]
        
        if prestamo.activo:
            self.service.devolver_material(prestamo.material._id)
            self.cargar_prestamos()

    # =========================================================
    # 7. MÓDULO RESERVAS
    # =========================================================

    # Funcion mostrar_reservas: realiza una parte del funcionamiento del programa
    def mostrar_reservas(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="📅 Reservas de Material",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)

        frame_tabla = tk.Frame(self.contenido, bg="#0f172a")
        frame_tabla.pack(fill="both", expand=True, padx=25, pady=15)

        self.tabla_reservas = ttk.Treeview(
            frame_tabla,
            columns=("Usuario", "Material", "Fecha"),
            show="headings",
        )
        self.tabla_reservas.pack(fill="both", expand=True)

        for col in ("Usuario", "Material", "Fecha"):
            self.tabla_reservas.heading(col, text=col)

        self.cargar_reservas()

        tk.Button(
            self.contenido,
            text="➕ Nueva Reserva",
            bg="#3b82f6",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            cursor="hand2",
            command=self.formulario_reserva
        ).pack(pady=10)

    # Funcion cargar_reservas: realiza una parte del funcionamiento del programa
    def cargar_reservas(self):
        for i in self.tabla_reservas.get_children():
            self.tabla_reservas.delete(i)

        for r in self.service.obtener_reservas():
            self.tabla_reservas.insert(
                "",
                "end",
                values=(
                    r.usuario._nombre,
                    r.material._titulo,
                    r.fecha.strftime("%d/%m/%Y")
                )
            )

    # Funcion formulario_reserva: realiza una parte del funcionamiento del programa
    def formulario_reserva(self):
        win = self.abrir_formulario("Nueva Reserva", alto=250)
        main = self.crear_scrollable_frame(win)

        tk.Label(main, text="ID Usuario", fg="white", bg="#0f172a").pack(anchor="w")
        u_id = tk.Entry(main, bg="#1f2937", fg="white")
        u_id.pack(fill="x", ipady=6)

        tk.Label(main, text="ID Material", fg="white", bg="#0f172a").pack(anchor="w", pady=(10, 0))
        m_id = tk.Entry(main, bg="#1f2937", fg="white")
        m_id.pack(fill="x", ipady=6)

        # Funcion realizar: realiza una parte del funcionamiento del programa
        def realizar():
            try:
                self.service.reservar_material(u_id.get(), m_id.get())
                self.cargar_reservas()
                win.destroy()
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", str(e))

        tk.Button(main, text="Reservar", bg="#3b82f6", fg="white", command=realizar).pack(fill="x", pady=20)

    # =========================================================
    # 8. MÓDULO INFORMES
    # =========================================================

    # Funcion mostrar_informes: realiza una parte del funcionamiento del programa
    def mostrar_informes(self):
        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="📊 Informes del Sistema",
            font=("Segoe UI", 20, "bold"),
            fg="white",
            bg="#0f172a"
        ).pack(pady=20)

        frame_info = tk.Frame(self.contenido, bg="#0f172a")
        frame_info.pack(fill="both", expand=True, padx=40)

        # Estadísticas básicas
        materiales = self.service.obtener_materiales()
        prestados = [m for m in materiales if not m.esta_disponible()]
        vencidos = [p for p in self.service.prestamos if p.activo and p.esta_vencido()]
        usuarios = self.service.obtener_usuarios()

        stats = [
            (f"👤 Total Usuarios: {len(usuarios)}", "#22c55e"),
            (f"📚 Total Materiales: {len(materiales)}", "#3b82f6"),
            (f"🤝 Préstamos Activos: {len(prestados)}", "#f59e0b"),
            (f"⚠️ Préstamos Vencidos: {len(vencidos)}", "#ef4444")
        ]

        if materiales:
            mas_usado = max(materiales, key=lambda m: m._veces_prestado)
            stats.append((f"🔥 Más Usado: {mas_usado._titulo} ({mas_usado._veces_prestado} veces)", "#f43f5e"))

        for texto, color in stats:
            f = tk.Frame(frame_info, bg="#1e293b", padx=20, pady=20)
            f.pack(fill="x", pady=10)
            tk.Label(f, text=texto, fg=color, bg="#1e293b", font=("Segoe UI", 14, "bold")).pack(side="left")