"""Ejercicio 17 — Una entrada incorrecta no termina el programa

Define pedir_entero(mensaje). Repite input hasta recibir un entero mayor o igual que cero. Si int falla, muestra "Escribe un entero". Si el valor es negativo, muestra "No puede ser negativo". Si es válido, devuélvelo. Introduce abc, -2, 0.

Comprueba: Hay dos avisos y la función devuelve 0. Una entrada vacía o "2.5" también debe volver a pedir el dato.

Ampliación: Define pedir_opcion(mensaje, maximo) que reutilice pedir_entero y rechace valores superiores al máximo.
"""

# Copia aquí tus clases de los ejercicios anteriores que se necesitan.


# 1. Definición de la función principal con bucle de validación
def pedir_entero(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada)
            if valor < 0:
                print("No puede ser negativo")
            else:
                return valor
        except ValueError:
            print("Escribe un entero")


# 2. Ampliación: Reutilizar pedir_entero y validar un máximo
def pedir_opcion(mensaje, maximo):
    while True:
        valor = pedir_entero(mensaje)
        if valor <= maximo:
            return valor
        print(f"El número no puede ser mayor que {maximo}")


# --- Pruebas y demostración ---

print("--- Ejercicio 17: Prueba de pedir_entero ---")
print("Para probar la secuencia requerida, ingresa consecutivamente: 'abc', '-2', '2.5', '' (vacío) y finalmente '0'.\n")

# Se solicita el dato hasta que la entrada sea válida (por ejemplo, 0)
resultado_entero = pedir_entero("Introduce un número entero (>= 0): ")
print(f"-> Valor válido obtenido: {resultado_entero}")


print("\n--- Ampliación: Prueba de pedir_opcion ---")
print("Probaremos limitar la entrada a un máximo de 3 (opciones válidas: 0, 1, 2, 3).\n")

opcion_seleccionada = pedir_opcion("Elige una opción (0 a 3): ", maximo=3)
print(f"-> Opción seleccionada correctamente: {opcion_seleccionada}")