import math

class Circulo:
    def __init__(self, radio):
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
