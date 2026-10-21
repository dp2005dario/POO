"""Ejercicio 03 — Datos que escribe una persona

Pide un título y un número de páginas con input. Convierte las páginas con int y muestra cuántas tendría el libro si se añadieran 10. En esta primera versión la entrada numérica será un entero válido. Anota qué ocurre al introducir "muchas" y conserva esa duda para el ejercicio 17.

Comprueba: Con Dune y 412, la nueva cantidad es 422. input devuelve texto incluso cuando escribes dígitos. "muchas" produce ValueError en esta versión.

Ampliación: Muestra cuánto ocuparían dos ejemplares si sumamos sus páginas.
"""



# Escribe tu solución debajo.
print("Dame un titulo y un numero de paginas, porfavor")

Titulo=input()
Paginas=input()

Paginas=int(Paginas)

print("Introduce nueva cantidad de paginas")
Paginas=input()
print(Paginas,type(Paginas))

#Ampliacion con dos ejemplares 

duplicacion_libro= Paginas*2

print(f"Dos ejemplares de: {Titulo}  Equivalen a :{duplicacion_libro}")

#Para este ejercicio he usado la funcion input que consiste como una entrada de texto que el usuario le pone de yipo string que mas tarde podremos reconvertir en int 
#en caso de que sea numero enteor ya que sino nos saldria un error de tipo ValueError y para finalizar para la duplcicacion de dicho libro he usado el simbolo * de multiplicacion