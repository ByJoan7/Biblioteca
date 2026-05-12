from services.biblioteca_service import BibliotecaService
from models.libro import Libro
from models.revista import Revista
from models.recurso_digital import RecursoDigital
from models.usuario import Socio, Bibliotecario, Administrador
import atexit


def menu_materiales(service):
    while True:
        print("\n--- MATERIALES ---")
        print("1. Ver todos")
        print("2. Agregar")
        print("3. Editar")
        print("4. Eliminar")
        print("5. Buscar")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            materiales = service.obtener_materiales()
            if not materiales:
                print("No hay materiales cargados.")
            else:
                for m in materiales:
                    print(m.descripcion_corta())

        elif opcion == "2":
            print("Tipo de material:")
            print("1. Libro")
            print("2. Revista")
            print("3. Recurso Digital")
            tipo = input("Seleccione una opcion: ")
            mid = input("ID: ")
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
                print("Material agregado.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            mid = input("ID del material a editar: ")
            material = service.materiales.get(mid)
            if not material:
                print("No se encontro el material.")
                continue
            print(f"Editando: {material.descripcion_corta()}")
            print("Deja en blanco lo que no quieras cambiar.")
            nuevos_datos = {}
            titulo = input(f"Titulo [{material._titulo}]: ")
            autor = input(f"Autor [{material._autor}]: ")
            categoria = input(f"Categoria [{material._categoria}]: ")
            if titulo:
                nuevos_datos["titulo"] = titulo
            if autor:
                nuevos_datos["autor"] = autor
            if categoria:
                nuevos_datos["categoria"] = categoria
            if hasattr(material, "_isbn"):
                isbn = input(f"ISBN [{material._isbn}]: ")
                if isbn:
                    nuevos_datos["isbn"] = isbn
            if hasattr(material, "_numero_edicion"):
                edicion = input(f"Edicion [{material._numero_edicion}]: ")
                if edicion:
                    nuevos_datos["numero_edicion"] = int(edicion)
            if hasattr(material, "_url"):
                url = input(f"URL [{material._url}]: ")
                if url:
                    nuevos_datos["url"] = url
            service.modificar_material(mid, nuevos_datos)
            print("Material actualizado.")

        elif opcion == "4":
            mid = input("ID del material a eliminar: ")
            confirmacion = input(f"Seguro que queres eliminar {mid}? (s/n): ")
            if confirmacion == "s":
                if service.eliminar_material(mid):
                    print("Material eliminado.")
                else:
                    print("No se encontro el material.")

        elif opcion == "5":
            print("Buscar por:")
            print("1. Titulo")
            print("2. Autor")
            print("3. Categoria")
            op2 = input("Seleccione una opcion: ")
            if op2 == "1":
                criterio = "titulo"
            elif op2 == "2":
                criterio = "autor"
            elif op2 == "3":
                criterio = "categoria"
            else:
                print("Opcion no valida.")
                continue
            valor = input("Buscar: ")
            resultados = service.buscar_materiales(criterio, valor)
            if resultados:
                for m in resultados:
                    print(m.descripcion_corta())
            else:
                print("No se encontraron resultados.")

        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_usuarios(service):
    while True:
        print("\n--- USUARIOS ---")
        print("1. Ver todos")
        print("2. Agregar")
        print("3. Editar")
        print("4. Eliminar")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            usuarios = service.obtener_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for u in usuarios:
                    print(u.descripcion_corta())

        elif opcion == "2":
            print("Tipo de usuario:")
            print("1. Socio")
            print("2. Bibliotecario")
            print("3. Administrador")
            tipo = input("Seleccione una opcion: ")
            uid = input("ID: ")
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

        elif opcion == "3":
            uid = input("ID del usuario a editar: ")
            usuario = service.usuarios.get(uid)
            if not usuario:
                print("No se encontro el usuario.")
                continue
            print(f"Editando: {usuario.descripcion_corta()}")
            nombre = input(f"Nombre [{usuario._nombre}]: ")
            if nombre:
                service.modificar_usuario(uid, {"nombre": nombre})
                print("Usuario actualizado.")

        elif opcion == "4":
            uid = input("ID del usuario a eliminar: ")
            confirmacion = input(f"Seguro que queres eliminar {uid}? (s/n): ")
            if confirmacion == "s":
                if service.eliminar_usuario(uid):
                    print("Usuario eliminado.")
                else:
                    print("No se encontro el usuario.")

        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_prestamos(service):
    while True:
        print("\n--- PRESTAMOS ---")
        print("1. Ver prestamos activos")
        print("2. Registrar prestamo")
        print("3. Registrar devolucion")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            activos = []
            for p in service.prestamos:
                if p.activo:
                    activos.append(p)
            if not activos:
                print("No hay prestamos activos.")
            else:
                for p in activos:
                    estado = "ACTIVO" if p.activo else "DEVUELTO"
                    multa = p.calcular_multa()
                    print(f"Usuario: {p.usuario._nombre} | Material: {p.material._titulo} | Vence: {p.fecha_vencimiento.strftime('%d/%m/%Y')} | Estado: {estado} | Multa: {multa}€")

        elif opcion == "2":
            uid = input("ID Usuario: ")
            mid = input("ID Material: ")
            dias = input("Dias de prestamo (dejar vacio para 14): ")
            if not dias:
                dias = 14
            else:
                dias = int(dias)
            try:
                service.prestar_material(uid, mid, dias)
                print("Prestamo realizado con exito.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            mid = input("ID Material a devolver: ")
            try:
                p = service.devolver_material(mid)
                multa = p.calcular_multa()
                if multa > 0:
                    print(f"Devolucion realizada. Multa por retraso: {multa:.2f} euros. El usuario fue sancionado.")
                else:
                    print("Devolucion realizada con exito.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_reservas(service):
    while True:
        print("\n--- RESERVAS ---")
        print("1. Ver reservas activas")
        print("2. Hacer una reserva")
        print("3. Cancelar una reserva")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            reservas = service.obtener_reservas()
            if not reservas:
                print("No hay reservas activas.")
            else:
                for r in reservas:
                    print(r.descripcion_corta())

        elif opcion == "2":
            uid = input("ID Usuario: ")
            mid = input("ID Material: ")
            try:
                service.reservar_material(uid, mid)
                print("Reserva registrada.")
            except Exception as e:
                print(f"Error: {e}")

        elif opcion == "3":
            uid = input("ID Usuario: ")
            mid = input("ID Material: ")
            if service.cancelar_reserva(uid, mid):
                print("Reserva cancelada.")
            else:
                print("No se encontro una reserva activa para ese usuario y material.")

        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_informes(service):
    while True:
        print("\n--- INFORMES ---")
        print("1. Materiales disponibles")
        print("2. Materiales prestados")
        print("3. Prestamos vencidos")
        print("4. Usuarios sancionados")
        print("5. Materiales mas prestados")
        print("0. Volver")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            items = service.informe_materiales_disponibles()
            print(f"\nMateriales disponibles ({len(items)}):")
            for m in items:
                print(m.descripcion_corta())

        elif opcion == "2":
            items = service.informe_materiales_prestados()
            print(f"\nMateriales prestados ({len(items)}):")
            for m in items:
                print(m.descripcion_corta())

        elif opcion == "3":
            items = service.informe_prestamos_vencidos()
            print(f"\nPrestamos vencidos ({len(items)}):")
            for p in items:
                print(f"Usuario: {p.usuario._nombre} | Material: {p.material._titulo} | Multa: {p.calcular_multa():.2f} euros")

        elif opcion == "4":
            items = service.informe_usuarios_sancionados()
            print(f"\nUsuarios sancionados ({len(items)}):")
            for u in items:
                print(u.descripcion_corta())

        elif opcion == "5":
            items = service.informe_materiales_mas_usados()
            print("\nTop 5 materiales mas prestados:")
            posicion = 1
            for m in items:
                usos = getattr(m, "_veces_prestado", 0)
                print(f"{posicion}. {m._titulo} - {usos} veces")
                posicion += 1

        elif opcion == "0":
            break
        else:
            print("Opcion no valida.")


def menu_consola():
    service = BibliotecaService()
    atexit.register(service.guardar_todo)

    while True:
        print("\n--- SISTEMA DE BIBLIOTECA ---")
        print("1. Materiales")
        print("2. Usuarios")
        print("3. Prestamos")
        print("4. Reservas")
        print("5. Informes")
        print("0. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_materiales(service)
        elif opcion == "2":
            menu_usuarios(service)
        elif opcion == "3":
            menu_prestamos(service)
        elif opcion == "4":
            menu_reservas(service)
        elif opcion == "5":
            menu_informes(service)
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu_consola()
