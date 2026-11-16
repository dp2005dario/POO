"""Taller 01 — Del préstamo al alta de ejemplares
Versión ampliada de la biblioteca del ejercicio 18.

Cambios respecto al ejercicio 18:
- Libro guarda el estado en self._disponible y lo expone con @property (solo lectura).
- Libro.codigo_valido(texto): método estático que valida etiquetas L01..L99.
- __init__ valida código y título y lanza ValueError si son incorrectos.
- Libro.desde_linea(linea): método de clase (constructor alternativo) para el escáner.
- Menú: nueva opción 5 «Alta desde escáner» y opción 6 «Consultar ficha».
- El catálogo empieza vacío (lo pide la prueba de aceptación del ejercicio 8).
"""

# ==========================================
# 1. CLASES BASE DE DOMINIO
# ==========================================

class Libro:
    """Ejemplar de la biblioteca. Conoce su estado y el formato de su código."""

    def __init__(self, codigo, titulo):
        # Misma regla que en todas las vías de alta: se reutiliza el validador estático.
        if not Libro.codigo_valido(codigo):
            raise ValueError(f"código no válido {codigo!r} (debe ser L01..L99)")
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("el título no puede estar vacío")
        self.codigo = codigo
        self.titulo = titulo
        self._disponible = True          # atributo interno (convenio: guion bajo)

    # --- Propiedad de solo lectura (ejercicio 3) ---
    @property
    def disponible(self):
        """Consulta el estado sin modificarlo. No tiene setter."""
        return self.disponible

    # --- Métodos de instancia: cambian el estado de ESTE ejemplar (self) ---
    def prestar(self):
        if not self._disponible:
            return False                 # intento rechazado: el estado no cambia
        self._disponible = False
        return True

    def devolver(self):
        if self._disponible:
            return False                 # intento rechazado: el estado no cambia
        self._disponible = True
        return True

    def resumen(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"[{self.codigo}] {self.titulo} - {estado}"

    # --- Método estático (ejercicio 4): solo necesita su argumento ---
    @staticmethod
    def codigo_valido(texto):
        """True si texto es una L mayúscula seguida de dos cifras ASCII, de 01 a 99."""
        if len(texto) != 3 or texto[0] != "L":
            return False
        if texto[1] not in "0123456789" or texto[2] not in "0123456789":
            return False
        return texto[1:] != "00"

    # --- Método de clase (ejercicio 5): constructor alternativo ---
    @classmethod
    def desde_linea(cls, linea):
        """Construye un ejemplar a partir de una línea del escáner: 'L08 ; Dune'."""
        if ";" not in linea:
            raise ValueError("falta el separador ';' entre código y título")
        codigo, titulo = linea.split(";", 1)     # solo el PRIMER punto y coma
        # La validación de código y título la hace el inicializador.
        return cls(codigo.strip(), titulo.strip())


class Biblioteca:
    """Conoce los códigos ya registrados (los duplicados se detectan aquí)."""

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


def alta_desde_escaner(biblio):
    """Opción 5. Lee una línea, construye el libro con el método de clase y lo añade."""
    linea = input("Línea del escáner (código;título): ")
    try:
        nuevo = Libro.desde_linea(linea)
    except ValueError as error:
        # El objeto no llega a existir: la colección no se toca.
        print(f"Alta rechazada: {error}.")
        return
    if not biblio.agregar(nuevo):
        # La biblioteca detecta el duplicado ANTES de añadirlo.
        print(f"Alta rechazada: el código {nuevo.codigo} ya está registrado.")
        return
    print(f"Alta correcta: {nuevo.resumen()}")


def consultar_ficha(biblio):
    """Opción 6. Solo LEE el estado: nunca llama a prestar() ni a devolver()."""
    codigo = input("Código del libro a consultar: ").strip()
    libro = biblio.buscar(codigo)
    if libro is None:
        print(f"Error: El libro [{codigo}] no existe en la biblioteca.")
    else:
        print(libro.resumen())


# ==========================================
# 3. APLICACIÓN DE CONSOLA (MENÚ)
# ==========================================

def menu_biblioteca():
    biblio = Biblioteca()   # catálogo vacío (prueba de aceptación del ejercicio 8)

    while True:
        print("\n--- MENÚ BIBLIOTECA ---")
        print("1. Listar todos los libros")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Listar solo libros disponibles")
        print("5. Alta desde escáner")
        print("6. Consultar ficha")
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

        elif opcion == 5:
            alta_desde_escaner(biblio)

        elif opcion == 6:
            consultar_ficha(biblio)

        elif opcion == 0:
            print("Saliendo de la aplicación...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    menu_biblioteca()
print(Libro("L01", "Dune").disponible)