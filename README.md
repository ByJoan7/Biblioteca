✅ 🧠 1. Qué debe hacer el programa (FUNCIONALIDAD OBLIGATORIA)
Tenéis que programar un sistema que permita:
📚 Materiales
Crear (alta) materiales
Modificar
Eliminar
Consultar
Tipos mínimos:
Libros
Revistas
Recursos digitales

👤 Usuarios
Registrar usuarios
Modificar
Eliminar
Consultar
Tipos posibles:
Socio
Bibliotecario
Administrador

🔄 Préstamos
Registrar préstamos
Registrar devoluciones
Controlar fechas
Detectar retrasos
Aplicar sanciones

📅 Reservas
Reservar materiales no disponibles
Gestionar cola de espera
Controlar caducidad

🔍 Búsquedas
Buscar por:
título
autor
categoría
disponibilidad

📊 Informes
Materiales disponibles
Materiales prestados
Préstamos vencidos
Usuarios sancionados
Materiales más usados

💾 Persistencia (MUY IMPORTANTE)
Guardar datos en archivo
Cargar datos al iniciar
👉 Si no guardáis datos → el proyecto está incompleto









🧱 2. Qué código te EXIGEN a nivel técnico (POO)
Aquí está lo que realmente evalúan:

🔹 Clases (obligatorio)
Debéis crear clases como mínimo:
Material (clase base)
Libro, Revista, etc. (herencia)
Usuario
Prestamo
Reserva

🔹 Herencia (obligatoria)
Ejemplo:
class Material:
class Libro(Material):
👉 Si no hay herencia bien usada → baja nota

🔹 Encapsulación
No todo debe ser público
Validar datos

🔹 Polimorfismo
Tratar distintos materiales de forma común

🔹 Relaciones entre objetos
Ejemplo:
Un Prestamo tiene:
un Usuario
un Material

🔹 Colecciones
Tenéis que usar:
listas
diccionarios
Ejemplo:
lista_materiales = []
lista_usuarios = []

🔹 Reglas de negocio (MUY importante)
Tenéis que programar lógica real, como:
No prestar si:
no hay disponibilidad
usuario sancionado
Límite de préstamos
Gestión de reservas
👉 Esto es de lo más importante del proyecto

🔹 Control de errores
Evitar que el programa “reviente”
Mensajes claros
(mejor si usáis excepciones propias)


🔹 Persistencia
Guardar en:
JSON ✅ (lo más fácil)
CSV
texto

🔹 Organización del código
NO todo en un archivo ❌
Separar por responsabilidades:
modelos
lógica
persistencia
interfaz

🔹 Interfaz
Menú por consola obligatorio
Ejemplo:
1. Ver materiales
2. Prestar
3. Devolver

🔹 Pruebas
Probar casos reales
Probar errores

🔹 Documentación
UML (diagrama de clases)
Memoria explicando:
decisiones
funcionamiento

📦 3. Qué tenéis que ENTREGAR
Esto también es obligatorio:
✅ Código completo funcionando
✅ Memoria técnica
✅ Diagrama UML
✅ Pruebas (ejemplos o capturas)
✅ Presentación oral
✅ Instrucciones de uso

⚠️ 4. Qué es lo MÁS importante (para nota)
Según el PDF:
✔️ Código limpio y bien organizado
✔️ Que funcione de verdad
✔️ Buen diseño de clases (POO)
✔️ Persistencia
✔️ Documentación clara

🧠 RESUMEN SIMPLE
Tenéis que programar:
👉 Un sistema de biblioteca que:
gestione materiales y usuarios
permita prestar, devolver y reservar
aplique reglas reales
guarde datos
tenga menú por consola
👉 Y hacerlo usando bien:
clases
herencia
lógica bien pensada
