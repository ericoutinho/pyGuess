import random

class pyGuess:

    def __init__(self, min=1, max=100):
        self.guess = 0
        self.max = max
        self.min = min
        self.random = 0
        self.tryNumber = 0
        self.hit = False
        self.getRandom()

    def start(self):
        print("")
        print("🍀 BEM-VINDO(A) AO ACERTE O NÚMERO [0 = EXIT]\n")
        try:
            self.getGuess()
            if self.guess != 0:
                while self.hit == False:
                    self.tryNumber += 1
                    if self.guess < self.random:
                        print(f"O número é maior que {self.guess}")
                        self.getGuess()
                    elif self.guess > self.random:
                        print(f"O número é menor que {self.guess}")
                        self.getGuess()
                    else:
                        n = str(self.tryNumber).zfill(3)
                        print( "------------------------------------------------------")
                        print(f"| Você acertou com {n} tentativas! Parabéns! 😎      |")
                        print( "------------------------------------------------------")
                        self.hit = True
            else:
                print("")
                print("😔 Ok. Goodbye!\n")
        except:
            print('😡 Favor digitar um número válido.')
            self.start()
    
    def getGuess(self):
        self.guess = int(input(f"Tente acertar um número entre {self.min} e {self.max}: "))

    def getRandom(self):
        self.random = random.randint(self.min, self.max)

myGuess = pyGuess(1,100)
myGuess.start()