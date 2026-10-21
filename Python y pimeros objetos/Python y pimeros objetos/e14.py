"""Ejercicio 14 — Dos nombres o dos objetos

Crea a = Libro("L1", "Dune"), b = a y c = Libro("L2", "Dune"). Antes de ejecutar b.prestar(), predice qué ocurrirá con a.disponible y c.disponible. Ejecuta y muestra a is b y a is c. is comprueba si dos referencias apuntan al mismo objeto.

Comprueba: a y b nombran el mismo objeto, que queda prestado. c es otro y sigue disponible. a is b es True y a is c es False.

Ampliación: Crea dos listas, copia = lista y separada = lista.copy(). Añade un elemento a copia y explica cuál de las dos listas cambia. La copia es superficial.
"""

# --- Clase Libro necesaria de ejercicios anteriores ---
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


# --- Ejercicio 14: Predicción y Comprobación ---

# Predicción inicial:
# 'a' y 'b' apuntan al MISMO objeto en memoria (son dos nombres para la misma referencia).
# Por tanto, ejecutar b.prestar() modificará la propiedad disponible tanto de 'b' como de 'a'.
# 'c' es un objeto NUEVO e independiente, por lo que su estado no cambiará y seguirá disponible.

# Creación de objetos y referencias
a = Libro("L1", "Dune")
b = a
c = Libro("L2", "Dune")

print("--- Ejercicio 14: Referencias e Identidad (is) ---")

# Estado inicial
print(f"Estado inicial -> a.disponible: {a.disponible}, b.disponible: {b.disponible}, c.disponible: {c.disponible}")

# Ejecutamos b.prestar()
b.prestar()

# Estado tras prestar desde 'b'
print("\nTras ejecutar b.prestar():")
print(f"a.disponible: {a.disponible}  (cambia porque 'a' y 'b' son el mismo objeto)")
print(f"b.disponible: {b.disponible}")
print(f"c.disponible: {c.disponible}  (no cambia porque 'c' es otro objeto distinto)")

# Comprobación de identidad con 'is'
print("\nComprobaciones de identidad:")
print(f"a is b -> {a is b} (Apuntan a la misma dirección de memoria)")
print(f"a is c -> {a is c} (Son objetos distintos en memoria)")


# --- Ampliación: Asignación vs .copy() en Listas ---

print("\n--- Ampliación: Listas y copia superficial ---")

lista_original = ["Dune", "1984"]
copia = lista_original
separada = lista_original.copy()

# Añadimos un elemento a 'copia'
copia.append("Fahrenheit 451")

print(f"lista_original : {lista_original}")
print(f"copia          : {copia}")
print(f"separada       : {separada}")

print(f"\n¿lista_original is copia? -> {lista_original is copia}")
print(f"¿lista_original is separada? -> {lista_original is separada}")
