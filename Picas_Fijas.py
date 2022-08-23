import random

class Agente:
    miNumero = 0
    picas = 0
    fijas = 0

    rondas = []
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
        
        self.picas = 0
        self.fijas = 0

    def compute(self, perception):
        response = self.switch(perception)
        return response
    
    def switch(perception):
        numbers = "0123456789"
        if (perception == "S"):
            self.setup()
            print(self.miNumero)
            return "R"
        elif (perception == "#"):
            return 
        elif (len(perception) == 4 and perception[0] in numbers and perception[1] in numbers and perception[2] in numbers and perception[3] in numbers):
            self.numeroRecibido(perception)
            return str(self.picas) + "," + str(self.fijas)
        elif (len(perception) == 3 and perception[0] in numbers and perception[1] == "," and perception[2] in numbers 
            and perception[0] + perception[2] >= 0 and perception[0] + perception[2] <= 4):
            return "A"
    
    def numeroRecibido(n):
        cifras = [digit for digit in self.miNumero]

        for i in range(len(perception)):
            if self.miNumero[i] == perception[i]:
                self.fijas += 1
                continue
            if perception[i] in cifras:
                self.picas += 1


class Ambiente:
    miAgente = Agente()
    miAgente2 = Agente()


def main():
    ambiente = Ambiente()
    return 0
