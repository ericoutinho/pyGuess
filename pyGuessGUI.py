import random
import PySimpleGUI as sg

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
        tentar = True
        layout = [
            [sg.Text(f'Digite um número entre {self.min} e {self.max}', size=(43,0))],
            [sg.InputText(key='inputGuess', size=(43, 0))],
            [sg.Button('Tentar'), sg.Button('Cancelar')],
            [sg.Output(size=(40, 10))]
        ]
        window = sg.Window("PyGuess", layout)
        while True:
            event, value = window.Read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == "Cancelar":
                window.close()
            if event == 'Tentar':
                self.guess = int(value['inputGuess'])
                while tentar == True:
                    if self.guess < self.random:
                        print(f"O número é maior que {self.guess}")
                        window.find('inputGuess').update('')
                        window.find('inputGuess').set_focus()
                        break
                    elif self.guess > self.random:
                        print(f"O número é menor que {self.guess}")
                        window.find('inputGuess').update('')
                        window.find('inputGuess').set_focus()
                        break
                    else:
                        tentar = False
                        print("Você acertou! Parabéns!")
                        window.find('inputGuess').update('')
                        window.find('inputGuess').set_focus()
                        break

    def getRandom(self):
        self.random = random.randint(self.min, self.max)

myGuess = pyGuess(1, 10)
myGuess.start()