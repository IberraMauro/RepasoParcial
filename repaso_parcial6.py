#--Ejercicio 6.1--#

def evitar_division_cero(function):
    def wrapper(a, b):
        if b == 0:
            print ("ERROR No se puede dividir por 0")
            return None
        else:
             return function(a, b)

    return wrapper

@evitar_division_cero
def funcion(a: float, b: float) ->float:
    return a / b

if __name__ == "__main__":
    print (funcion(40,0))
    print (funcion(120,7))

#--Ejercicio 6.2--#
from datetime import datetime

def saludar(function):
    def wrapper():
        print ("Hola")
        function()
        print ("Ciao")
    return wrapper

def con_fecha_hora(function):
    def wrapper():
        ahora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        print (f"Fecha y hora actual --> {ahora}")
        function()
    return wrapper

@saludar
@con_fecha_hora
def tipico():
    print ("Estoy por estudiar")

respuesta = """Se ejecuta en orden descendente desde el primer decorador
va bajando hasta la funcion a decorar, esta funcion seria el centro,
luego en orden ascendente sube hasta el primer decorador y termina."""

if __name__ == "__main__":
    tipico()



from complemento6 import uno, dos

print ()
@uno
@dos
def saludo():
    print ("¿Funciono?")

respuesta2 = """Se importa a la funcion desde el modulo correspondiente,
y luego se arrobea.
"""

if __name__ == "__main__":
    saludo()


