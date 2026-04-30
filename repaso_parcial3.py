#--Ejercicio 3.1--#

#Es composcicion porque la clase se crea dentro la clase#

class Memoria:
    def __init__(self, capacidad: float) ->None:
        self.capacidad = capacidad


class Procesador:
    def __init__(self, velocidad: float) ->None:
        self.velocidad = velocidad


class Computadora:
    def __init__(self, m_capacidad: float, p_velocidad: float) ->None:
        self.m_capacidad = Memoria(m_capacidad)
        self.p_velocidad = Procesador(p_velocidad)

    def ficha_tecnica(self):
        print (f"Capacidad de memoria: {self.m_capacidad.capacidad} TB")
        print (f"Velocidad de procesador: {self.p_velocidad.velocidad} Ghz")

if __name__ == "__main__":
    a = Computadora(250, 1895)
    a.ficha_tecnica()


#--Ejercicio 3.2--#

class Cancion:
    def __init__(self, titulo: str, autor: str) ->None:
        self.titulo = titulo
        self.autor = autor


class Playlist:
    playlist = []

    def agregar_cancion(self, cancion: Cancion):
        self.playlist.append(cancion)
        print ("Cancion agregada")

    def cantidad(self):
        a = len(self.playlist)
        print (f"La playlist tiene {a} canciones.")

    def listar(self):
        if not self.playlist:
            print ("Playlist vacia")

        else:
            for x in self.playlist:
                print (f"Cancion {x.titulo} de {x.autor}")


if __name__ == "__main__":
    c1 = Cancion("Bohemian Rhapsody", "Queen")
    c2 = Cancion("Yesterday", "The Beatles")
    c3 = Cancion("Like a Rolling Stone", "Bob Dylan")
    c4 = Cancion("Respect", "Aretha Franklin")

    p = Playlist()

    p.agregar_cancion(c1)
    p.agregar_cancion(c2)
    p.agregar_cancion(c3)
    p.agregar_cancion(c4)

    p.listar()
    p.cantidad()











