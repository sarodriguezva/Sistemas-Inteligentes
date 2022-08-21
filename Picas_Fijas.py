import random

class Agente:
    miNumero = 0

    def __init__(self):
        self.setup()
        print(self.miNumero)

    #Setea de forma aleatoria el número con el que jugará
    def setup(self):
        self.miNumero = str(random.randint(0,9999))
        cifras = [int(digit) for digit in self.miNumero]
        lista = []

        #Si un número es menor de 4 cifras lo completa con ceros al inicio.
        if len(cifras) < 4:
            self.miNumero = str(0)*(4-len(cifras)) + str(self.miNumero)
            for i in range(4-len(cifras)):
                cifras.insert(0, 0)

        #Revisa si hay cifras repetidas, de haberlas, vuelve a setear el número
        for cifra in cifras:
            if cifra in lista:
                self.setup()
                break
            else:
                lista.append(cifra)

    def compute(self):
        return 0

class Ambiente:
    miAgente = Agente()
    miAgente2 = Agente()


def main():
    ambiente = Ambiente()
    return 0
