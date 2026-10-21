"""Ejercicio 12 — Nuestra primera clase

Crea tu propia clase Libro. Su inicializador recibe codigo y titulo, guarda ambos en self y establece disponible = True. Crea L1 con Dune y L2 con 1984. Muestra sus títulos. En esta versión añadimos un código para distinguir ejemplares incluso si comparten título.

Comprueba: L1 y L2 tienen códigos y títulos independientes. Ambos empiezan disponibles. Cambiar el título del primero no cambia el segundo.

Ampliación: Añade autor al inicializador y crea dos objetos con autores diferentes.
"""



# 1. Definición de la clase con la ampliación (código, título y autor)
class Libro:
    """Clase para representar ejemplares de libros con código de identificación."""
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.disponible = True


# 2. Creación de las instancias L1 y L2
L1 = Libro("LIB001", "Dune", "Frank Herbert")
L2 = Libro("LIB002", "1984", "George Orwell")


# --- Comprobaciones ---

print("--- Ejercicio 12: Creación de objetos independientes ---")

# Mostrar atributos iniciales
print(f"L1 -> Código: {L1.codigo} | Título: {L1.titulo} | Autor: {L1.autor} | Disponible: {L1.disponible}")
print(f"L2 -> Código: {L2.codigo} | Título: {L2.titulo} | Autor: {L2.autor} | Disponible: {L2.disponible}")

print("\n--- Demostración de independencia de estado ---")

# Cambiamos el título de L1
L1.titulo = "Dune: Parte Uno"

print(f"Nuevo título de L1: {L1.titulo}")
print(f"Título de L2 tras modificar L1: {L2.titulo}")