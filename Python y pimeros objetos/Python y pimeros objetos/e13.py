"""Ejercicio 13 — Métodos que cumplen una regla

Añade prestar y devolver a tu clase. prestar devuelve True y cambia disponible a False solo si estaba disponible. En caso contrario devuelve False y conserva el estado. devolver hace la operación inversa y también informa con un booleano. Usa la clase en cuatro llamadas: prestar, prestar, devolver, devolver.

Comprueba: Las llamadas devuelven True, False, True, False. El estado final es disponible. Un intento rechazado no altera el objeto.

Ampliación: Añade resumen, equivalente a etiqueta del ejercicio 11 pero sin parámetro libro: usa self.
"""



class Libro:
    """Clase para representar ejemplares de libros con estado de préstamo."""
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
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

    # Ampliación: Método resumen equivalente a etiqueta pero usando self
    def resumen(self):
        estado = "disponible" if self.disponible else "prestado"
        return f"{self.titulo} [{estado}]"


# --- Comprobaciones y secuencia de pruebas ---

print("--- Ejercicio 13: Métodos prestar, devolver y resumen ---")

# Creación de una instancia de prueba
libro_prueba = Libro("LIB001", "Dune", "Frank Herbert")

print(f"Estado inicial: {libro_prueba.resumen()}")
print("-" * 40)

# Secuencia de 4 llamadas requerida:
r1 = libro_prueba.prestar()   # 1. Prestar libro disponible -> True
print(f"1. prestar()  -> Devuelve: {r1:<5} | Estado actual: {libro_prueba.resumen()}")

r2 = libro_prueba.prestar()   # 2. Prestar libro YA prestado -> False
print(f"2. prestar()  -> Devuelve: {r2:<5} | Estado actual: {libro_prueba.resumen()}")

r3 = libro_prueba.devolver()  # 3. Devolver libro prestado -> True
print(f"3. devolver() -> Devuelve: {r3:<5} | Estado actual: {libro_prueba.resumen()}")

r4 = libro_prueba.devolver()  # 4. Devolver libro YA disponible -> False
print(f"4. devolver() -> Devuelve: {r4:<5} | Estado actual: {libro_prueba.resumen()}")

print("-" * 40)
print(f"¿Estado final disponible?: {libro_prueba.disponible}")