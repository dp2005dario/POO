"""Ejercicio 11 — Una función recibe un objeto

Define etiqueta(libro). Devuelve "Dune [disponible]" o "Dune [prestado]" según el título y estado del objeto recibido. Crea un Libro preparado y muestra su etiqueta antes y después de prestarlo. La función etiqueta no debe modificarlo.

Comprueba: La etiqueta cambia después del préstamo. El objeto mantiene el mismo título. Consultarlo no lo presta.

Ampliación: Define prestar_y_etiquetar(libro), que intente prestarlo y devuelva su etiqueta. Explica qué función consulta y cuál modifica.
"""



class Libro:
    """Modelo preparado para aprender a usar objetos."""
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponible = True

    def prestar(self):
        if not self.disponible:
            return False
        self.disponible = False
        return True

    def resumen(self):
        if self.disponible:
            estado = "disponible"
        else:
            estado = "prestado"
        return f"{self.titulo}: {estado}"


# 1. Definición de la función etiqueta (solo consulta)
def etiqueta(libro):
    estado = "disponible" if libro.disponible else "prestado"
    return f"{libro.titulo} [{estado}]"


# 2. Definición de la ampliación (modifica el objeto)
def prestar_y_etiquetar(libro):
    libro.prestar()
    return etiqueta(libro)


# --- Comprobaciones y pruebas ---

# Creación del objeto
mi_libro = Libro("Dune")

print("--- Ejercicio 11: Función etiqueta ---")
print("Antes de prestar:")
print(etiqueta(mi_libro))  # Imprime: Dune [disponible]

# Demostramos que consultarlo no lo presta
print("\nConsultamos la etiqueta otra vez:")
print(etiqueta(mi_libro))  # Sigue imprimiendo: Dune [disponible]

# Prestamos el libro usando su método propio
mi_libro.prestar()

print("\nDespués de prestarlo:")
print(etiqueta(mi_libro))  # Imprime: Dune [prestado]


print("\n--- Ampliación: prestar_y_etiquetar ---")
otro_libro = Libro("1984")

print("Estado inicial:")
print(etiqueta(otro_libro))  # Imprime: 1984 [disponible]

print("\nEjecutamos prestar_y_etiquetar:")
resultado = prestar_y_etiquetar(otro_libro)
print(f"Resultado devuelto: {resultado}")  # Imprime: 1984 [prestado]

print("\nVerificamos el objeto tras la llamada:")
print(etiqueta(otro_libro))  # Se confirma que cambió su estado interno