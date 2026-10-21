"""Ejercicio 16 — Una biblioteca contiene libros

Define Biblioteca con self.libros = [] en __init__. Añade buscar(codigo), agregar(libro) y prestar(codigo). agregar rechaza códigos repetidos y devuelve un booleano. prestar busca el objeto y delega en su método prestar. Si no lo encuentra, devuelve False. Un mismo título con códigos distintos sí se admite.

Comprueba: Agregar L1 funciona una vez. Agregar otro L1 falla sin reemplazar el anterior. Prestar L9 falla. Dos bibliotecas nuevas no comparten su lista.

Ampliación: Añade total_disponibles que devuelva cuántos libros disponibles tiene la biblioteca.
"""

# --- Clase Libro de ejercicios anteriores ---
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


# --- Clase Biblioteca (Ejercicio 16) ---
class Biblioteca:
    def __init__(self):
        self.libros = []

    def buscar(self, codigo):
        for libro in self.libros:
            if libro.codigo == codigo:
                return libro
        return None

    def agregar(self, libro):
        # Rechazar si ya existe un libro con el mismo código
        if self.buscar(libro.codigo) is not None:
            return False
        self.libros.append(libro)
        return True

    def prestar(self, codigo):
        libro = self.buscar(codigo)
        if libro is None:
            return False
        # Delegar la acción al método prestar del objeto Libro
        return libro.prestar()

    # Ampliación: Contar cuántos libros disponibles existen
    def total_disponibles(self):
        contador = 0
        for libro in self.libros:
            if libro.disponible:
                contador += 1
        return contador


# --- Comprobaciones y Secuencia de Pruebas ---

print("--- Ejercicio 16: Clase Biblioteca ---")

# Creación de la biblioteca y libros de prueba
b1 = Biblioteca()
l1 = Libro("L1", "Dune")
l1_duplicado = Libro("L1", "Dune (Edición Especial)")
l2 = Libro("L2", "1984")
l3 = Libro("L3", "Dune")  # Mismo título que l1, pero distinto código

# 1. Comprobar que agregar L1 funciona la primera vez
r_agregar_1 = b1.agregar(l1)
print(f"1. Agregar L1 primera vez: {r_agregar_1}")  # True

# 2. Comprobar que agregar un código repetido falla y no reemplaza el anterior
r_agregar_2 = b1.agregar(l1_duplicado)
print(f"2. Agregar otro L1 (código duplicado): {r_agregar_2}")  # False
print(f"   Libro almacenado en L1: {b1.buscar('L1').titulo}")  # Sigue siendo "Dune"

# 3. Mismo título con distinto código sí se admite
b1.agregar(l2)
b1.agregar(l3)
print(f"3. Agregar L3 (mismo título, distinto código): True")

# 4. Intentar prestar un código inexistente (L9)
r_prestar_l9 = b1.prestar("L9")
print(f"4. Prestar código inexistente 'L9': {r_prestar_l9}")  # False

# 5. Prestar un libro existente (L1)
r_prestar_l1 = b1.prestar("L1")
print(f"5. Prestar 'L1' existente: {r_prestar_l1}")  # True

print("\n--- Comprobación de independencia entre Bibliotecas ---")

b2 = Biblioteca()
print(f"Libros en b1: {len(b1.libros)}")  # 3
print(f"Libros en b2: {len(b2.libros)}")  # 0
print(f"¿Comparten la misma lista?: {b1.libros is b2.libros}")  # False


print("\n--- Ampliación: total_disponibles ---")

print(f"Total de libros en b1: {len(b1.libros)}")
print(f"Total de disponibles en b1: {b1.total_disponibles()}")  # Debe dar 2 (L2 y L3, ya que L1 está prestado)
