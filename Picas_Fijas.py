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

    def compute(self, perception):
        if type(perception) is not str:
            print("Entrada no se puede procesar.")
            return

        picas = 0
        fijas = 0
        cifras = [digit for digit in self.miNumero]

        for i in range(len(perception)):
            if self.miNumero[i] == perception[i]:
                fijas += 1
                continue
            if perception[i] in cifras:
                picas += 1

        return [picas, fijas]

class Ambiente:
    miAgente = Agente()
    miAgente2 = Agente()


def main():
    ambiente = Ambiente()
    return 0
