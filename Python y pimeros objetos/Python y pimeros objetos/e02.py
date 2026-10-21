"""Ejercicio 02 — Un cálculo de existencias

Una biblioteca tiene 12 ejemplares y ha prestado 5. Calcula cuántos quedan y qué porcentaje representan. Guarda ambos resultados y muéstralos con un texto. Usa una cadena f para incluir valores, por ejemplo f"Quedan {restantes}". Supón que el total es positivo.

Comprueba: Quedan 7 ejemplares. El porcentaje es aproximadamente 58,33. Si prestados vale 0, quedan 12 y el porcentaje es 100.

Ampliación: Calcula cuántas cajas de 5 ejemplares se llenan con los 12 y cuántos sobran.
"""



# Escribe tu solución debajo.
Libros_biblioteca = 12
Libros_prestamos = 5
restantes = Libros_biblioteca - Libros_prestamos
porcentaje = (restantes / Libros_biblioteca) * 100

print(f"Quedan {restantes} ejemplares.")

print(f"El porcentaje es aproximadamente {porcentaje:.2f}%.")
cajas = Libros_biblioteca // 5
sobrantes = Libros_biblioteca % 5
print(f"Se llenan {cajas} cajas de 5 ejemplares y sobran {sobrantes} ejemplares.")

#primeramente he creado 3 variables para saber el total  de libros, los restantes y los prestados, luego otra avriable con una operación
#Para saber el porcentaje de los sobrantes y ya por último para la ampliación he usado el simbolo \\ para hacer la division y mas abajo el de € para saber el resto de la division