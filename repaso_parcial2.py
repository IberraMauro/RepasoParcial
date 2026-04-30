#--Ejercicio 2.1--#
import math

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

#--Ejercicio 2.2--#
print()





