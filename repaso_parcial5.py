#--Ejercicio 5.1--#

#Punto
def initP(self, x: int, y:int ) ->None:
    self.x = x
    self.y = y

def eje_x(self):
    print (f"El punto cruza por el eje X en {self.x}")

def eje_y(self):
    print (f"El punto cruza por el eje Y en {self.y}")

def impresion(self):
    return (f"({self.x},{self.y})")

def opuesto(self):
    return type(self)(self.x * -1, self.y * -1)


#Linea
def initL(self, punto_a: object, punto_b: object) ->None:
    self.punto_a = punto_a
    self.punto_b = punto_b

def mueve_derecha(self, num: float):
    if num >= 0:
        self.punto_a.x += num
        self.punto_b.x += num

def mueve_izquierda(self, num: float):
    if num >= 0:
        self.punto_a.x -= num
        self.punto_b.x -= num

def mueve_arriba(self, num: float):
    if num >= 0:
        self.punto_a.y += num
        self.punto_b.y += num

def mueve_abajo(self, num: float):
    if num >= 0:
        self.punto_a.y -= num
        self.punto_b.y -= num


#Cancion7
def initC(self, titulo: str, autor: str) ->None:
    self.titulo = titulo
    self.autor = autor

def get_titulo(self):
    return (self.titulo)

def get_autor(self):
    return (self.autor)

def set_titulo(self, titulo: str):
    self.titulo = titulo

def set_autor(self, autor: str):
    self.autor = autor

if __name__ == "__main__":

    Punto = type("Punto", (), {
    "__init__": initP,
    "eje_x": eje_x,
    "eje_y": eje_y,
    "impresion":impresion,
    "opuesto": opuesto
    })

    Linea = type("Linea", (), dict(
    __init__ = initL,
    mueve_derecha = mueve_derecha,
    mueve_izquierda = mueve_izquierda,
    mueve_arriba = mueve_arriba,
    mueve_abajo = mueve_abajo
    ))

    Cancion = type("Cancion", (), dict(
    __init__ = initC,
    get_titulo = get_titulo,
    get_autor = get_autor,
    set_titulo = set_titulo,
    set_autor = set_autor
    ))






