import random

class Agente:
    miNumero = ""
    guess = ""
    rondas = {}
    options = "0123456789"

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
        
        self.guess = ""
        self.rondas = {}
        self.options = "0123456789"

    def compute(self, perception):
        response = self.switch(perception)
        return response
    
    def switch(self, perception):
        numbers = "0123456789"
        if (perception == "S"):
            #Iniciar juego
            self.setup()
            print(self.miNumero)
            return "R"
        
        elif (perception == "#"):
            #Número del rival que debo adivinar
            if len(self.rondas) == 0:
                self.guess = "0123"
                return self.guess
            elif len(self.rondas) == 1:
                self.guess = "4567"
                return self.guess
            elif (len(self.rondas) == 2):
                t1 = self.rondas.get("0123")
                t2 = self.rondas.get("4567")
                t1s = t1[0] + t1[1]
                t2s = t2[0] + t2[1]
                suma = t1s + t2s
                
                if suma == 4:
                    self.options = "01234567"
                    
                elif suma <= 4:
                    return
                
            return
        
        elif (len(perception) == 4 and perception[0] in numbers and perception[1] in numbers and perception[2] in numbers and perception[3] in numbers):
            #Picas y fijas de mi número
            (picas, fijas) = self.inputNumber(perception)
            return str(picas) + "," + str(fijas)
        
        elif (len(perception) == 3 and perception[0] in numbers and perception[1] == "," and perception[2] in numbers 
            and int(perception[0]) + int(perception[2]) >= 0 and int(perception[0]) + int(perception[2]) <= 4):
            #Guardar número de picas y fijas del rival
            self.rondas.update({self.guess : (int(perception[0]), int(perception[2]))})  
            return "A"
        
        else:
            return "Elemento recibido no puede ser procesado."
    
    def inputNumber(self, n):
        picas = 0
        fijas = 0
        cifras = [digit for digit in self.miNumero]

        for i in range(len(perception)):
            if self.miNumero[i] == perception[i]:
                self.fijas += 1
                continue
            if perception[i] in cifras:
                self.picas += 1
        
        return (picas, fijas)


class Ambiente:
    miAgente = Agente()
    miAgente2 = Agente()


def main():
    ambiente = Ambiente()
    return 0
