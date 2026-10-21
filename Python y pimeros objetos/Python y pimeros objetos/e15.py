"""Ejercicio 15 — Buscar entre objetos

Crea una lista con L1 Dune y L2 1984. Define buscar(libros, codigo): devuelve el objeto cuyo código coincide o None si no existe. Prueba L1 y L9. Solo llama a prestar cuando el resultado no sea None.

Comprueba: Buscar L1 devuelve el propio objeto almacenado. Buscar L9 devuelve None. Prestar el resultado de L1 modifica el objeto de la lista.

Ampliación: Define disponibles(libros) que construya y devuelva una lista con los libros disponibles.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# --- Clase Libro necesaria de los ejercicios anteriores ---
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

    def resumen(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"[{self.codigo}] {self.titulo} - {estado}"


# 1. Función buscar(libros, codigo)
def buscar(libros, codigo):
    for libro in libros:
        if libro.codigo == codigo:
            return libro
    return None


# 2. Ampliación: Función disponibles(libros)
def disponibles(libros):
    lista_disponibles = []
    for libro in libros:
        if libro.disponible:
            lista_disponibles.append(libro)
    return lista_disponibles


# --- Comprobaciones y pruebas ---

# Creación de objetos y lista contenedora
L1 = Libro("L1", "Dune")
L2 = Libro("L2", "1984")
biblioteca = [L1, L2]

print("--- Ejercicio 15: Buscar entre objetos ---")

# Búsqueda con un código existente (L1)
resultado_l1 = buscar(biblioteca, "L1")
print(f"Búsqueda 'L1': {resultado_l1.resumen() if resultado_l1 else 'No encontrado'}")

# Búsqueda con un código inexistente (L9)
resultado_l9 = buscar(biblioteca, "L9")
print(f"Búsqueda 'L9': {resultado_l9}")

print("\n--- Intento de préstamo condicional (evitando AttributeError) ---")

# Prestar L1 tras comprobar que no es None
if resultado_l1 is not None:
    resultado_l1.prestar()
    print("Se prestó el libro encontrado con éxito.")

# Comprobamos que el objeto original dentro de la lista cambió
print(f"Estado de L1 en la lista tras el préstamo: {biblioteca[0].resumen()}")

# Intento seguro con L9
if resultado_l9 is not None:
    resultado_l9.prestar()
else:
    print("No se pudo prestar 'L9' porque el resultado es None.")


print("\n--- Ampliación: Obtener lista de disponibles ---")

# L2 sigue disponible, L1 ya no
libros_libres = disponibles(biblioteca)

print("Libros disponibles actualmente:")
for libro in libros_libres:
    print(f"- {libro.resumen()}")