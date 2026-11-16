"""Pruebas del taller (ejercicios 1, 3, 4, 5 y 6).
Ejecuta: python pruebas.py   (debe estar en la misma carpeta que biblioteca.py)
"""
from biblioteca import Libro

# ------------------------------------------------------------
print("=== Ejercicio 1 · Dos ejemplares ===")
# Predicción: True False / False False / True
a = Libro("L01", "Dune")
b = Libro("L02", "Dune")
print(a.prestar(), a.disponible)
print(a.prestar(), a.disponible)
print(b.disponible)
# Si fuera b = a, b sería el MISMO objeto y saldría False.

# ------------------------------------------------------------
print("\n=== Ejercicio 3 · Experimento de encapsulación ===")
a = Libro("L01", "Dune")
try:
    a.disponible = False
except AttributeError as error:
    print("a.disponible = False ->", type(error).__name__, ":", error)

a2 = Libro("L01", "Dune")          # ejecución independiente
a2._disponible = False             # funciona: el _ es solo un convenio
print("Tras a2._disponible = False, a2.disponible =", a2.disponible,
      "(se ha saltado prestar(): no hay préstamo registrado)")

# ------------------------------------------------------------
print("\n=== Ejercicio 4 · Comprobaciones del validador ===")
# Se llaman sobre la clase, SIN crear ningún objeto.
assert Libro.codigo_valido("L01") is True
assert Libro.codigo_valido("L99") is True
for texto in ["L00", "L1", "L001", "l03", " L03", "L٣٤", ""]:
    assert Libro.codigo_valido(texto) is False, texto
print("Tabla del validador: todas las comprobaciones correctas")

try:
    Libro("L00", "Dune")
    print("ERROR: debería haber fallado")
except ValueError as error:
    print('Libro("L00", "Dune") -> ValueError:', error)
assert Libro("L01", " Dune ").titulo == "Dune"
print('Libro("L01", " Dune ").titulo == "Dune" -> True')
try:
    Libro("L05", "   ")
except ValueError as error:
    print('Libro("L05", "   ") -> ValueError:', error)

# ------------------------------------------------------------
print("\n=== Ejercicio 5 · Alta desde el escáner ===")
x = Libro.desde_linea(" L08 ; Dune ")
print(repr(x.codigo), repr(x.titulo))
y = Libro.desde_linea("L09; Python; casos prácticos")
print("Título completo:", repr(y.titulo))
for linea in ["L10", "L00;Dune", "L10;  "]:
    try:
        Libro.desde_linea(linea)
    except ValueError as error:
        print(f"{linea!r:12} -> rechazada: {error}")


class LibroDeSala(Libro):
    pass


ejemplar = LibroDeSala.desde_linea("L11;Atlas")
print("Prueba de la subclase:", type(ejemplar).__name__)   # LibroDeSala (con cls)

# ------------------------------------------------------------
print("\n=== Ejercicio 6 · Referencias ===")
libro = Libro("L14", "Atlas")
inventario = [libro]
mostrador = libro
del libro
mostrador.prestar()
print(inventario[0].disponible)   # False
del mostrador
print(inventario[0].titulo)       # Atlas
inventario.clear()                # desaparece la última referencia
