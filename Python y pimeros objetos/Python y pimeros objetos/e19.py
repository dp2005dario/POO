"""Ejercicio 19 — Guardar y recuperar el catálogo

Extensión opcional hacia RA3. Define guardar(biblioteca, ruta) y cargar(ruta). Guarda una lista de diccionarios con codigo, titulo y disponible. Al cargar, crea una nueva Biblioteca y nuevos Libro, recuperando el estado mediante prestar si corresponde. En este ejercicio el JSON tiene el formato esperado y códigos únicos. Préstale L1, guarda, carga y comprueba su estado.

Comprueba: La nueva biblioteca conserva títulos, códigos y disponibilidad, pero contiene instancias nuevas. Un título con tildes se conserva. JSON almacena datos, no los métodos del objeto.

Ampliación: Si el fichero no existe, devuelve una biblioteca vacía. Un JSON dañado debe seguir mostrando su error, sin ocultarlo.
"""

import json

# --- Clases Base (Ejercicio 16) ---
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


class Biblioteca:
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
            return False
        return libro.prestar()


# ==========================================
# FUNCIONES DE PERSISTENCIA (JSON)
# ==========================================

def guardar(biblioteca, ruta):
    """Convierte el estado de los objetos a una lista de diccionarios y la guarda en JSON."""
    datos = []
    for libro in biblioteca.libros:
        datos.append({
            "codigo": libro.codigo,
            "titulo": libro.titulo,
            "disponible": libro.disponible
        })
    
    # ensure_ascii=False conserva caracteres como tildes o 'ñ' sin escaparlos
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)


def cargar(ruta):
    """
    Carga el JSON y reconstruye una nueva Biblioteca con nuevas instancias de Libro.
    Maneja FileNotFoundError (fichero inexistente) devolviendo una biblioteca vacía.
    Permite que los errores de JSON dañado (json.JSONDecodeError) se propaguen.
    """
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except FileNotFoundError:
        # Ampliación: Si el fichero no existe, devuelve una biblioteca vacía
        return Biblioteca()

    # Reconstrucción de la biblioteca con nuevos objetos
    nueva_biblio = Biblioteca()
    for item in datos:
        libro = Libro(item["codigo"], item["titulo"])
        if not item["disponible"]:
            libro.prestar()  # Recupera el estado prestado si corresponde
        nueva_biblio.agregar(libro)

    return nueva_biblio


# ==========================================
# COMPROBACIONES Y PRUEBAS
# ==========================================

print("--- Ejercicio 19: Guardar y Cargar Catálogo ---")

ruta_archivo = "biblioteca.json"

# 1. Crear biblioteca original con títulos que incluyen tildes
biblio_original = Biblioteca()
l1 = Libro("L1", "Dune: Crónicas")
l2 = Libro("L2", "Cien años de soledad")
biblio_original.agregar(l1)
biblio_original.agregar(l2)

# 2. Prestar L1
biblio_original.prestar("L1")
print("Estado original de L1 en biblio_original:")
print(f"  {biblio_original.buscar('L1').resumen()}")

# 3. Guardar estado en archivo JSON
guardar(biblio_original, ruta_archivo)
print(f"\n[+] Catálogo guardado con éxito en '{ruta_archivo}'.")

# 4. Cargar estado en una NUEVA instancia de Biblioteca
biblio_recuperada = Biblioteca()
biblio_recuperada = cargar(ruta_archivo)

# 5. Comprobaciones de estado e independencia de instancias
libro_l1_recuperado = biblio_recuperada.buscar("L1")
libro_l2_recuperado = biblio_recuperada.buscar("L2")

print("\nEstado tras la carga en biblio_recuperada:")
print(f"  {libro_l1_recuperado.resumen()}")
print(f"  {libro_l2_recuperado.resumen()}")

print("\n--- Verificación de Independencia (Instancias Nuevas) ---")
print(f"¿Mismo objeto L1 en memoria?: {l1 is libro_l1_recuperado}")  # False
print(f"¿Misma biblioteca en memoria?: {biblio_original is biblio_recuperada}")  # False


print("\n--- Ampliación: Fichero Inexistente vs JSON Dañado ---")

# Prueba A: Fichero que no existe
biblio_inexistente = cargar("archivo_fantasma.json")
print(f"Cargar fichero inexistente -> Devuelve biblioteca con {len(biblio_inexistente.libros)} libros.")

# Prueba B: Fichero JSON dañado
ruta_danado = "danado.json"
with open(ruta_danado, "w", encoding="utf-8") as f:
    f.write("{ este json está roto ...")

print("\nIntentando cargar fichero JSON dañado (debe mostrar el error sin ocultarlo):")
try:
    cargar(ruta_danado)
except json.JSONDecodeError as e:
    print(f"  -> Error capturado correctamente (JSONDecodeError): {e.msg}")
