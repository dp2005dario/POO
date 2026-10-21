"""Ejercicio 10 — Una función que calcula

Define dias_restantes(plazo, transcurridos). Debe devolver la resta, sin imprimirla ni cambiar los argumentos. Llama a la función y muestra el resultado desde fuera. Prueba (14, 4), (14, 14) y (14, 17).

Comprueba: Los resultados son 10, 0 y -3. return entrega un valor que se puede guardar. print solo lo muestra.

Ampliación: Define estado_plazo(plazo, transcurridos), reutilizando dias_restantes, que devuelva En plazo, Vence hoy o Con retraso.
"""



# 1. Definición de la función principal
def dias_restantes(plazo, transcurridos):
    return plazo - transcurridos

# 2. Definición de la ampliación reutilizando dias_restantes
def estado_plazo(plazo, transcurridos):
    restantes = dias_restantes(plazo, transcurridos)
    
    if restantes > 0:
        return "En plazo"
    elif restantes == 0:
        return "Vence hoy"
    else:
        return "Con retraso"

# --- Comprobaciones desde fuera de las funciones ---

casos_prueba = [(14, 4), (14, 14), (14, 17)]

print("--- Ejercicio 10: días restantes ---")
for plazo, transcurridos in casos_prueba:
    resultado = dias_restantes(plazo, transcurridos)
    print(f"dias_restantes({plazo}, {transcurridos}) -> {resultado}")

print("\n--- Ampliación: estado del plazo ---")
for plazo, transcurridos in casos_prueba:
    estado = estado_plazo(plazo, transcurridos)
    print(f"estado_plazo({plazo}, {transcurridos}) -> {estado}")