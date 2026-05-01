def uno(funcion):
    def envoltura():
        print("Antes de uno")
        funcion()
        print("Despues de uno")
    return envoltura

def dos(funcion):
    def envoltura():
        print("Antes de dos")
        funcion()
        print("Despues de dos")
    return envoltura
