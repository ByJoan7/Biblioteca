# Archivo: console_main.py
# Este archivo forma parte del sistema de biblioteca.
import random
import atexit
from services.biblioteca_service import BibliotecaService
from models.libro import Libro
from models.revista import Revista
from models.recurso_digital import RecursoDigital
from models.usuario import Socio, Bibliotecario, Administrador


# genera un id de 4 cifras que no se repita
# Funcion generar_id: realiza una parte del funcionamiento del programa
def generar_id(existentes):
    while True:
        nuevo = str(random.randint(1000, 9999))
        if nuevo not in existentes:
            return nuevo


# Funcion menu_materiales: realiza una parte del funcionamiento del programa
def menu_materiales(service):
    while True:
        print("\n--- MATERIALES ---")
        print("1. Ver todos")
        print("2. Agregar")
        print("3. Editar")
        print("4. Eliminar")
        print("5. Buscar")
        print("0. Volver")
        op = input("Opcion: ")

        if op == "1":
            materiales = service.obtener_materiales()
            if not materiales:
                print("No hay materiales.")
            else:
                for m in materiales:
                    print(m.descripcion_corta())

        elif op == "2":
            print("Que tipo de material es?")
            print("1. Libro")
            print("2. Revista")
            print("3. Recurso digital")
            tipo = input("Opcion: ")
            mid = generar_id(list(service.materiales.keys()))
            print(f"ID asignado: {mid}")
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            try:
                if tipo == "1":
                    isbn = input("ISBN: ")
                    material = Libro(mid, titulo, autor, categoria, isbn)
                elif tipo == "2":
                    edicion = input("Numero de edicion: ")
                    material = Revista(mid, titulo, autor, categoria, int(edicion))
                elif tipo == "3":
                    url = input("URL: ")
                    formato = input("Formato (ebook/audio/video/articulo/otro): ")
                    material = RecursoDigital(mid, titulo, autor, categoria, url, formato)
                else:
                    print("Opcion no valida.")
                    continue
                service.agregar_material(material)
                print("Material agregado correctamente.")
            except Exception as e:
                print(f"Error: {e}")

        elif op == "3":
            materiales = service.obtener_materiales()
            if not materiales:
                print("No hay materiales.")
                continue
            for i, m in enumerate(materiales):
                print(f"{i + 1}. {m.descripcion_corta()}")
            num = input("Que material queres editar? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(materiales):
                print("Numero no valido.")
                continue
            material = materiales[int(num) - 1]
            print("Dejalo en blanco si no lo queres cambiar.")
            nuevos = {}
            titulo = input(f"Titulo [{material._titulo}]: ")
            autor = input(f"Autor [{material._autor}]: ")
            categoria = input(f"Categoria [{material._categoria}]: ")
            if titulo:
                nuevos["titulo"] = titulo
            if autor:
                nuevos["autor"] = autor
            if categoria:
                nuevos["categoria"] = categoria
            if hasattr(material, "_isbn"):
                isbn = input(f"ISBN [{material._isbn}]: ")
                if isbn:
                    nuevos["isbn"] = isbn
            if hasattr(material, "_numero_edicion"):
                ed = input(f"Edicion [{material._numero_edicion}]: ")
                if ed:
                    nuevos["numero_edicion"] = int(ed)
            if hasattr(material, "_url"):
                url = input(f"URL [{material._url}]: ")
                if url:
                    nuevos["url"] = url
            service.modificar_material(material._id, nuevos)
            print("Material actualizado.")

        elif op == "4":
            materiales = service.obtener_materiales()
            if not materiales:
                print("No hay materiales.")
                continue
            for i, m in enumerate(materiales):
                print(f"{i + 1}. {m.descripcion_corta()}")
            num = input("Que material queres eliminar? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(materiales):
                print("Numero no valido.")
                continue
            material = materiales[int(num) - 1]
            confirm = input(f"Estas seguro que queres eliminar '{material._titulo}'? (s/n): ")
            if confirm == "s":
                service.eliminar_material(material._id)
                print("Material eliminado.")

        elif op == "5":
            print("Buscar por:")
            print("1. Titulo")
            print("2. Autor")
            print("3. Categoria")
            op2 = input("Opcion: ")
            if op2 == "1":
                criterio = "titulo"
            elif op2 == "2":
                criterio = "autor"
            elif op2 == "3":
                criterio = "categoria"
            else:
                print("Opcion no valida.")
                continue
            valor = input("Que queres buscar?: ")
            resultados = service.buscar_materiales(criterio, valor)
            if resultados:
                for m in resultados:
                    print(m.descripcion_corta())
            else:
                print("No se encontro nada.")

        elif op == "0":
            break
        else:
            print("Opcion no valida.")


# Funcion menu_usuarios: realiza una parte del funcionamiento del programa
def menu_usuarios(service):
    while True:
        print("\n--- USUARIOS ---")
        print("1. Ver todos")
        print("2. Agregar")
        print("3. Editar")
        print("4. Eliminar")
        print("0. Volver")
        op = input("Opcion: ")

        if op == "1":
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for u in usuarios:
                    print(u.descripcion_corta())

        elif op == "2":
            print("Que tipo de usuario es?")
            print("1. Socio")
            print("2. Bibliotecario")
            print("3. Administrador")
            tipo = input("Opcion: ")
            uid = generar_id(list(service.usuarios.keys()))
            print(f"ID asignado: {uid}")
            nombre = input("Nombre: ")
            try:
                if tipo == "1":
                    num_socio = input("Numero de socio: ")
                    usuario = Socio(uid, nombre, num_socio)
                elif tipo == "2":
                    num_empleado = input("Numero de empleado: ")
                    usuario = Bibliotecario(uid, nombre, num_empleado)
                elif tipo == "3":
                    usuario = Administrador(uid, nombre)
                else:
                    print("Opcion no valida.")
                    continue
                service.agregar_usuario(usuario)
                print("Usuario registrado.")
            except Exception as e:
                print(f"Error: {e}")

        elif op == "3":
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios.")
                continue
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u.descripcion_corta()}")
            num = input("Que usuario queres editar? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(usuarios):
                print("Numero no valido.")
                continue
            usuario = usuarios[int(num) - 1]
            nombre = input(f"Nombre [{usuario._nombre}]: ")
            if nombre:
                service.modificar_usuario(usuario._id, {"nombre": nombre})
                print("Usuario actualizado.")

        elif op == "4":
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios.")
                continue
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u.descripcion_corta()}")
            num = input("Que usuario queres eliminar? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(usuarios):
                print("Numero no valido.")
                continue
            usuario = usuarios[int(num) - 1]
            confirm = input(f"Estas seguro que queres eliminar a {usuario._nombre}? (s/n): ")
            if confirm == "s":
                service.eliminar_usuario(usuario._id)
                print("Usuario eliminado.")

        elif op == "0":
            break
        else:
            print("Opcion no valida.")


# Funcion menu_prestar: realiza una parte del funcionamiento del programa
def menu_prestar(service):
    while True:
        print("\n--- PRESTAR ---")
        print("1. Ver lo que esta prestado")
        print("2. Prestar un material")
        print("3. Devolver un material")
        print("0. Volver")
        op = input("Opcion: ")

        if op == "1":
            activos = []
            for p in service.prestamos:
                if p.activo:
                    activos.append(p)
            if not activos:
                print("No hay nada prestado ahora mismo.")
            else:
                for p in activos:
                    print(p.descripcion_corta())

        elif op == "2":
            # mostrar usuarios
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
                continue
            print("\nUsuarios:")
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u.descripcion_corta()}")
            num = input("Selecciona el usuario (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(usuarios):
                print("Numero no valido.")
                continue
            usuario = usuarios[int(num) - 1]

            # mostrar materiales disponibles para prestar
            disponibles = []
            for m in service.obtener_materiales():
                if m.esta_disponible():
                    disponibles.append(m)
            if not disponibles:
                print("No hay materiales disponibes para prestar.")
                continue
            print("\nMateriales disponibles para prestar:")
            for i, m in enumerate(disponibles):
                print(f"{i + 1}. {m.descripcion_corta()}")
            num2 = input("Selecciona el material (numero): ")
            if not num2.isdigit() or int(num2) < 1 or int(num2) > len(disponibles):
                print("Numero no valido.")
                continue
            material = disponibles[int(num2) - 1]

            dias = input("Cuantos dias se va a prestar? (enter para 14): ")
            if not dias:
                dias = 14
            else:
                dias = int(dias)
            try:
                service.prestar_material(usuario._id, material._id, dias)
                print(f"Se presto '{material._titulo}' a {usuario._nombre}.")
            except Exception as e:
                print(f"Error: {e}")

        elif op == "3":
            activos = []
            for p in service.prestamos:
                if p.activo:
                    activos.append(p)
            if not activos:
                print("No hay nada prestado ahora mismo.")
                continue
            print("\nLo que esta prestado:")
            for i, p in enumerate(activos):
                print(f"{i + 1}. {p.descripcion_corta()}")
            num = input("Cual se esta devolviendo? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(activos):
                print("Numero no valido.")
                continue
            prestamo = activos[int(num) - 1]
            try:
                p = service.devolver_material(prestamo.material._id)
                multa = p.calcular_multa()
                if multa > 0:
                    print(f"Devolucion con retraso. Multa: {multa:.2f} euros. Usuario sancionado.")
                else:
                    print("Devolucion realizada.")
            except Exception as e:
                print(f"Error: {e}")

        elif op == "0":
            break
        else:
            print("Opcion no valida.")


# Funcion menu_reservas: realiza una parte del funcionamiento del programa
def menu_reservas(service):
    while True:
        print("\n--- RESERVAS ---")
        print("1. Ver reservas activas")
        print("2. Hacer una reserva")
        print("3. Cancelar una reserva")
        print("0. Volver")
        op = input("Opcion: ")

        if op == "1":
            reservas = service.obtener_reservas()
            if not reservas:
                print("No hay reservas activas.")
            else:
                for r in reservas:
                    print(r.descripcion_corta())

        elif op == "2":
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios.")
                continue
            print("\nUsuarios:")
            for i, u in enumerate(usuarios):
                print(f"{i + 1}. {u.descripcion_corta()}")
            num = input("Selecciona el usuario (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(usuarios):
                print("Numero no valido.")
                continue
            usuario = usuarios[int(num) - 1]

            materiales = service.obtener_materiales()
            if not materiales:
                print("No hay materiales.")
                continue
            print("\nMateriales:")
            for i, m in enumerate(materiales):
                print(f"{i + 1}. {m.descripcion_corta()}")
            num2 = input("Selecciona el material (numero): ")
            if not num2.isdigit() or int(num2) < 1 or int(num2) > len(materiales):
                print("Numero no valido.")
                continue
            material = materiales[int(num2) - 1]
            try:
                service.reservar_material(usuario._id, material._id)
                print("Reserva realizada.")
            except Exception as e:
                print(f"Error: {e}")

        elif op == "3":
            reservas = service.obtener_reservas()
            if not reservas:
                print("No hay reservas activas.")
                continue
            for i, r in enumerate(reservas):
                print(f"{i + 1}. {r.descripcion_corta()}")
            num = input("Cual queres cancelar? (numero): ")
            if not num.isdigit() or int(num) < 1 or int(num) > len(reservas):
                print("Numero no valido.")
                continue
            reserva = reservas[int(num) - 1]
            if service.cancelar_reserva(reserva.usuario._id, reserva.material._id):
                print("Reserva cancelada.")
            else:
                print("No se pudo cancelar.")

        elif op == "0":
            break
        else:
            print("Opcion no valida.")


# Funcion menu_informes: realiza una parte del funcionamiento del programa
def menu_informes(service):
    while True:
        print("\n--- INFORMES ---")
        print("1. Materiales disponibles")
        print("2. Materiales prestados")
        print("3. Vencidos con multa")
        print("4. Usuarios sancionados")
        print("5. Los mas prestados")
        print("0. Volver")
        op = input("Opcion: ")

        if op == "1":
            items = service.informe_materiales_disponibles()
            print(f"Materiales disponibles ({len(items)}):")
            for m in items:
                print(m.descripcion_corta())

        elif op == "2":
            items = service.informe_materiales_prestados()
            print(f"Materiales prestados ahora mismo ({len(items)}):")
            for m in items:
                print(m.descripcion_corta())

        elif op == "3":
            items = service.informe_prestamos_vencidos()
            print(f"Prestados con fecha vencida ({len(items)}):")
            for p in items:
                print(p.descripcion_corta())

        elif op == "4":
            items = service.informe_usuarios_sancionados()
            print(f"Usuarios sancionados ({len(items)}):")
            for u in items:
                print(u.descripcion_corta())

        elif op == "5":
            items = service.informe_materiales_mas_usados()
            print("Top 5:")
            pos = 1
            for m in items:
                usos = getattr(m, "_veces_prestado", 0)
                print(f"{pos}. {m._titulo} - prestado {usos} veces")
                pos += 1

        elif op == "0":
            break
        else:
            print("Opcion no valida.")


# Funcion menu_consola: realiza una parte del funcionamiento del programa
def menu_consola():
    service = BibliotecaService()
    atexit.register(service.guardar_todo)

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Materiales")
        print("2. Usuarios")
        print("3. Prestar")
        print("4. Reservas")
        print("5. Informes")
        print("0. Salir")
        op = input("Opcion: ")

        if op == "1":
            menu_materiales(service)
        elif op == "2":
            menu_usuarios(service)
        elif op == "3":
            menu_prestar(service)
        elif op == "4":
            menu_reservas(service)
        elif op == "5":
            menu_informes(service)
        elif op == "0":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu_consola()