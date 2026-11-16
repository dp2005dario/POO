"""Ejercicio 7 — El testigo del inventario (archivo independiente).
Ejecuta: python testigo.py 1   -> primer guion
         python testigo.py 2   -> segundo guion (con copia)
"""
import sys


class Testigo:
    def __init__(self, codigo):
        self.codigo = codigo
        if codigo == "L20":
            print(f"Alta {self.codigo}")

    def __del__(self):
        print(f"Fin {self.codigo}")


def guion_1():
    testigo = Testigo("L20")
    caja = [testigo]
    del testigo
    print("A: la caja conserva", caja[0].codigo)
    caja.clear()
    print("B: la caja está vacía")


def guion_2():
    testigo = Testigo("L20")
    caja = [testigo]
    del testigo
    print("A: la caja conserva", caja[0].codigo)
    copia = caja[0]              # referencia adicional ANTES de vaciar la caja
    caja.clear()
    print("B: la caja está vacía")
    print(copia.codigo)
    del copia


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "2":
        guion_2()
    else:
        guion_1()
