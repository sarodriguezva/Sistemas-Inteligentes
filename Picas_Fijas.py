import random
from itertools import permutations

class Agente:
    miNumero = ""
    digitos = "0123456789"
    guess = ""
    opciones = []
    respuestas = []
    scores = []

    def __init__(self):
        self.setup()

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
                return
            else:
                lista.append(cifra)

        self.guess = ""
        self.opciones = list(permutations(self.digitos, 4))
        random.shuffle(self.opciones)

    def compute(self, perception):
        response = self.switch(perception)
        return response

    def switch(self, perception):
        numbers = "0123456789"
        if perception == "S":
            #Iniciar juego
            self.setup()
            print(self.miNumero)
            return "R"

        elif perception == "#":
            #Número del rival que debo adivinar
            self.guess = self.opciones[0]
            self.respuestas.append(self.guess)
            return "".join(self.guess)

        elif len(perception) == 4 and perception[0] in numbers and perception[1] in numbers and perception[2] in numbers and perception[3] in numbers:
            #Picas y fijas de mi número
            (picas, fijas) = self.inputNumber(perception)
            return str(picas) + "," + str(fijas)

        elif (len(perception) == 3 and perception[0] in numbers and perception[1] == "," and perception[2] in numbers
              and 0 <= int(perception[0]) + int(perception[2]) <= 4):
            #Guardar número de picas y fijas del rival
            score = (int(perception[0]), int(perception[2]))
            self.scores.append(score)
            self.opciones = [c for c in self.opciones if self.relativeScore(c, self.guess) == score]
            return "A"

        else:
            return "Elemento recibido no puede ser procesado."

    def inputNumber(self, n):
        picas = 0
        fijas = 0
        cifras = [digit for digit in self.miNumero]

        for i in range(len(n)):
            if self.miNumero[i] == n[i]:
                fijas += 1
            elif n[i] in cifras:
                picas += 1

        return picas, fijas

    def relativeScore(self, guess, chosen):
        fijas = picas = 0
        for g, c in zip(guess, chosen):
            if g == c:
                fijas += 1
            elif g in chosen:
                picas += 1
        return picas, fijas


class Ambiente:
    miAgente = Agente()

    while True:
        entrada = input("Esperando entrada ")
        print(miAgente.compute(entrada))


def main():
    ambiente = Ambiente()
    return 0
