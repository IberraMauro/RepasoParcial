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


class Animal:
    def __init__(self, nombre: str, edad: int) ->None:
        self._nombre = nombre      # encapsulamiento (convención con guion bajo)
        self._edad = edad

    def get_nombre(self):          # getter
        return self._nombre

    def get_edad(self):
        return self._edad

    def hablar(self):              # abstracción: las hijas la implementan
        raise NotImplementedError("Las subclases deben implementar hablar()")


class Perro(Animal):               # herencia
    def hablar(self):              # polimorfismo (override)
        return "Guau!"


class Gato(Animal):
    def hablar(self):
        return "Miau!"


class Vaca(Animal):
    def hablar(self):
        return "Muu!"


class Pato(Animal):
    def hablar(self):
        return "Quack!"


class Oveja(Animal):
    def hablar(self):
        return "Bee soy un clon!"


animales = [Perro("Toby", 3), Gato("Michi", 5), Vaca("Lola", 4), Pato("Patricio", 2), Oveja("Dolly", 0)]
for a in animales:
    print(f"{a.get_nombre()} ({a.get_edad()} años) dice: {a.hablar()}")





