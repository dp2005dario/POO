"""Ejercicio 18 — La biblioteca de consola

Prepara una Biblioteca con L1 Dune y L2 1984. Implementa un menú: 1 listar, 2 prestar, 3 devolver y 0 salir. Reutiliza pedir_entero. Para préstamo o devolución solicita un código y distingue libro inexistente de operación rechazada. La interfaz muestra mensajes, pero cambia el estado llamando a métodos. Puedes copiar tus clases y funciones en el mismo archivo.

Comprueba: No debe fallar al introducir abc como opción. Rechaza prestar dos veces L1 y devolver dos veces L1. L9 se informa como inexistente. Al salir termina el bucle. Los datos se pierden al reiniciar: todavía no hay persistencia.

Ampliación: Añade la opción 4 para listar solo los disponibles.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# ==========================================
# 1. CLASES BASE DE DOMINIO
# ==========================================

class Libro:
    def __init__(self, codigo, titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        return False

    def resumen(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"[{self.codigo}] {self.titulo} - {estado}"


class Biblioteca:
    def __init__(self):
        self.libros = []

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def agregar(self, libro):
        if self.buscar(libro.codigo) is not None:
            return False
        self.libros.append(libro)
        return True

    def prestar(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            return "inexistente"
        if libro.prestar():
            return "exito"
        return "ya_prestado"

    def devolver(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            return "inexistente"
        if libro.devolver():
            return "exito"
        return "ya_disponible"

    def obtener_todos(self):
        return self.libros

    def obtener_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]


# ==========================================
# 2. FUNCIONES DE INTERFAZ Y ENTRADA
# ==========================================

def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < 0:
                print("No puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Escribe un entero válido.")


# ==========================================
# 3. APLICACIÓN DE CONSOLA (MENÚ)
# ==========================================

def menu_biblioteca():
    # Inicialización de la biblioteca y carga inicial de datos
    biblio = Biblioteca()
    biblio.agregar(Libro("L1", "Dune"))
    biblio.agregar(Libro("L2", "1984"))

    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Listar todos los libros")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Listar solo libros disponibles")  # Ampliación
        print("0. Salir")

        opcion = pedir_entero("Selecciona una opción: ")

        if opcion == 1:
            print("\n--- Listado Completo ---")
            libros = biblio.obtener_todos()
            if not libros:
                print("La biblioteca está vacía.")
            else:
                for libro in libros:
                    print(libro.resumen())

        elif opcion == 2:
            codigo = input("Introduce el código del libro a prestar: ").strip()
            resultado = biblio.prestar(codigo)

            if resultado == "exito":
                print(f"El libro [{codigo}] ha sido prestado con éxito.")
            elif resultado == "ya_prestado":
                print(f"Operación rechazada: El libro [{codigo}] ya se encuentra prestado.")
            elif resultado == "inexistente":
                print(f"Error: El libro [{codigo}] no existe en la biblioteca.")

        elif opcion == 3:
            codigo = input("Introduce el código del libro a devolver: ").strip()
            resultado = biblio.devolver(codigo)

            if resultado == "exito":
                print(f"El libro [{codigo}] ha sido devuelto con éxito.")
            elif resultado == "ya_disponible":
                print(f"Operación rechazada: El libro [{codigo}] ya estaba disponible.")
            elif resultado == "inexistente":
                print(f"Error: El libro [{codigo}] no existe en la biblioteca.")

        elif opcion == 4:
            print("\n--- Libros Disponibles ---")
            disponibles = biblio.obtener_disponibles()
            if not disponibles:
                print("No hay libros disponibles en este momento.")
            else:
                for libro in disponibles:
                    print(libro.resumen())

        elif opcion == 0:
            print("Saliendo de la aplicación...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecución del programa interactivo
if __name__ == "__main__":
    menu_biblioteca()