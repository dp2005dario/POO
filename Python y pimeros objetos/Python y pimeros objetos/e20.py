"""Ejercicio 20 — La misma llamada con respuestas distintas

Extensión opcional de RA2. Crea Material con titulo y descripcion(), que devuelve el título. LibroPapel y Revista heredan de Material y redefinen descripcion para anteponer "Libro: " y "Revista: ". Recorre una lista con un objeto de cada tipo y llama a descripcion sin comprobar su tipo.

Comprueba: La misma llamada produce "Libro: Dune" y "Revista: Ciencia". El bucle no conoce los detalles de cada clase.

Ampliación: Añade AudioLibro y comprueba que funciona en el mismo bucle sin modificarlo.
"""
# 1. Clase base / superclase
class Material:
    def __init__(self, titulo):
        self.titulo = titulo

    def descripcion(self):
        return self.titulo


# 2. Subclases que heredan de Material y redefinen el método (Polimorfismo)
class LibroPapel(Material):
    def descripcion(self):
        return f"Libro: {self.titulo}"


class Revista(Material):
    def descripcion(self):
        return f"Revista: {self.titulo}"


# 3. Ampliación: Subclase AudioLibro
class AudioLibro(Material):
    def descripcion(self):
        return f"AudioLibro: {self.titulo}"


# --- Comprobaciones y Secuencia de Pruebas ---

print("--- Ejercicio 20: Herencia y Polimorfismo ---")

# Creación de una lista heterogénea de materiales
catalogo = [
    LibroPapel("Dune"),
    Revista("Ciencia"),
    AudioLibro("1984")  # Incorporación de la ampliación
]

# Recorrido del bucle polimórfico
print("Recorriendo el catálogo con la misma llamada (.descripcion()):\n")

for material in catalogo:
    # La llamada es idéntica para todos los elementos, sin comprobar el tipo (type/isinstance)
    print(material.descripcion())
