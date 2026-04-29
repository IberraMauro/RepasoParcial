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


#--Ejercicio 2--#
print ()

class Figura:
    def area(self):
        raise NotImplementedError("No se polimorfeo area()")

class Cuadrado(Figura):
    def __init__(self, base: float) ->None:
        self.base = base

    def area(self):
        return self.base ** 2

class Triangulo(Figura):
    def __init__(self, base: float, altura: float) ->None:
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Circulo2(Figura):
    def __init__(self, radio: float) -> None:
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)

lista_ej2 = [Cuadrado(15), Triangulo(12, 6), Circulo2(24), Circulo2(9.6), Cuadrado(9.5), Triangulo(10, 8)]

for x in lista_ej2:
    print(x.area())
