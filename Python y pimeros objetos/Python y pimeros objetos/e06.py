"""Ejercicio 06 — Una decisión sobre el plazo

Usa dias = 3 como número de días que faltan para devolver un libro. Si dias es mayor que 0, muestra "En plazo". Si es 0, "Vence hoy". Si es negativo, "Con retraso". Prueba también 0 y -2 cambiando la variable.

Comprueba: 3 produce En plazo, 0 produce Vence hoy y -2 produce Con retraso. Solo se ejecuta una rama.

Ampliación: Para un retraso, muestra además cuántos días han pasado desde el vencimiento.
"""



# Escribe tu solución debajo.
# Cambia este valor a 0 o a -2 para probar los distintos resultados
dias = 3 

if dias > 0:
    print("En plazo")
elif dias == 0:
    print("Vence hoy")
else:
    print("Con retraso")
    # Ampliación: Mostrar cuántos días han pasado
    # Multiplicamos por -1 (o usamos abs()) para mostrar el número en positivo
    dias_pasados = -dias 
    print(f"Han pasado {dias_pasados} días desde el vencimiento.")