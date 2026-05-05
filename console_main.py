from services.biblioteca_service import BibliotecaService
from models.libro import Libro
from models.usuario import Usuario

def menu_consola():
    service = BibliotecaService()
    
    while True:
        print("\n--- SISTEMA DE BIBLIOTECA (CONSOLA) ---")
        print("1. Ver Materiales")
        print("2. Ver Préstamos")
        print("3. Prestar Material")
        print("4. Devolver Material")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            for m in service.obtener_materiales():
                print(f"[{m._id}] {m._titulo} - {m._autor} ({'Disponible' if m.esta_disponible() else 'Prestado'})")
        
        elif opcion == "2":
            for p in service.prestamos:
                estado = "ACTIVO" if p.activo else "DEVUELTO"
                multa = p.calcular_multa()
                print(f"Usuario: {p.usuario._nombre} | Libro: {p.material._titulo} | Vence: {p.fecha_vencimiento.strftime('%d/%m/%Y')} | Estado: {estado} | Multa: {multa}€")
        
        elif opcion == "3":
            u_id = input("ID Usuario: ")
            m_id = input("ID Material: ")
            try:
                service.prestar_material(u_id, m_id)
                print("Préstamo realizado con éxito")
            except Exception as e:
                print(f"Error: {e}")
                
        elif opcion == "4":
            m_id = input("ID Material a devolver: ")
            try:
                service.devolver_material(m_id)
                print("Devolución realizada con éxito")
            except Exception as e:
                print(f"Error: {e}")
                
        elif opcion == "5":
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_consola()
