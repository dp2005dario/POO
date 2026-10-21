"""Ejercicio 05 — Dos objetos de una clase preparada

Guarda modelos_inicio.py en la misma carpeta. Escribe from modelos_inicio import Libro. Crea a = Libro("Dune") y b = Libro("1984"). Muestra a.titulo y los resultados de a.resumen() y b.resumen(). Explica qué comparten y qué distingue a los dos libros.

Comprueba: Los dos son de la clase Libro, pero sus títulos son distintos. Ambos comienzan disponibles.

Ampliación: Crea un tercer libro titulado "Fundación" y muestra su resumen.
"""


# Escribe tu solución debajo.
from modelos_inicio import Libro

# --- Solución ---

# 1. Creamos los dos objetos de la clase Libro
a = Libro("Dune")
b = Libro("1984")

# 2. Mostramos el título del primer libro y los resúmenes de ambos
print(f"Título del primer libro: {a.titulo}")
print(f"Resumen de a: {a.resumen()}")
print(f"Resumen de b: {b.resumen()}")

# --- Ampliación ---

# 3. Creamos un tercer libro y mostramos su resumen
c = Libro("Fundación")
print(f"Resumen del tercer libro (Ampliación): {c.resumen()}")