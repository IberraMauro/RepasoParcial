#--Ejercicio 1.1--#
import math

class Circulo:
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

    def diametro(self):
        return 2 * self.radio


c1 = Circulo(5)
c2 = Circulo(2)

print (F"Area: {c1.area()}, Perimetro: {c1.perimetro()}, Diametro: {c1.diametro()}")
print ()
print (F"Area: {c2.area()}, Perimetro: {c2.perimetro()}, Diametro: {c2.diametro()}")


#--Ejercicio 1.2--#

class CuentaBancaria:
    def __init__(self, titular: str, saldo: float) -> None:
        self.titular = titular
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, nuevo):
        if nuevo < 0:
            print ("ERROR")
        else:
            self._saldo = nuevo

    def depositar(self, monto: float):
        if monto > 0:
            self.saldo += monto
            print ("Saldo depositado")
        else:
            print ("ERROR")

    def extraer(self, monto: float):
        if (self.saldo - monto) < 0:
            print ("Error saldo insuficiente")
        else:
            self.saldo -= monto
            print ("Monto retirado")

    def consultar_saldo(self):
        print (f"Saldo: {self.saldo}")

