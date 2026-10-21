"""Ejercicio 04 — Los textos tienen métodos

Parte de titulo = "  dune  ". Predice y ejecuta titulo.strip() y titulo.upper(). Guarda el resultado de strip en limpio y el de upper aplicado a limpio en mayusculas. Muestra los tres nombres con repr para ver sus espacios. No encadenes todavía las llamadas.

Comprueba: titulo mantiene sus espacios y minúsculas. limpio vale "dune" y mayusculas vale "DUNE".

Ampliación: Compara los títulos " Dune " y "dune" ignorando espacios exteriores y mayúsculas.
"""



# Escribe tu solución debajo.

titulo = " dune "
limpio =titulo.strip()
limpio_mayusculas= titulo.upper()

print("Comprobacion")
print(titulo)
print(limpio)
print(limpio_mayusculas)

#Ampliacion
titulo_a = " Dune "
titulo_b = "dune"

igual=titulo_a.strip().lower() ==titulo_b.strip().lower()

print(f"Los titulos {titulo_a} y {titulo_b} son iguales: {igual}")

#En este ejercicio he usado los nuevos metodos de strip y upper que sirven para eliminar los espacios y ponerlo en mayusuclas y mas abajos para compararlos los he convertido ambos sin espacios y en minusculas
#Y con la variable igual hemos hecho una comparacion  en la que nos sale impreso en pantalla un true de que la condicion se cumple.