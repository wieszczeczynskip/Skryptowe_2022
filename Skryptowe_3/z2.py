class Portfel:
    zlote = 0
    dolary = 0
    euro = 0

    def printPortfel(self):
        print(f'Ilosc zlotych: {self.zlote}')
        print(f'Ilosc dolarow: {self.dolary}')
        print(f'Ilosc euro: {self.euro}')

    def sumaPLN(self):
        return self.zlote + 4.75*self.euro + 4.3*self.dolary

    def setPLN(self, x):
        if isinstance(x, (int, float)):
            self.zlote = x

portfele = []
portfele.append(Portfel())
portfele.append(Portfel())
portfele.append(Portfel())
portfele.append(Portfel())
for x in portfele:
    x.printPortfel()
print("===========================")
portfele[0].zlote = 10
portfele[0].dolary = 20
portfele[0].euro = 30
portfele[1].zlote = 40
portfele[1].dolary = 50
portfele[1].euro = 60
portfele[2].zlote = 70
portfele[2].dolary = 80
portfele[2].euro = 90
portfele[3].zlote = 100
portfele[3].dolary = 200
portfele[3].euro = 300
for x in portfele:
    x.printPortfel()
print("===========================")
portfele[3].setPLN("999")
for x in portfele:
    x.printPortfel()
print("===========================")
print("Wartosc portfela: " + str(portfele[0].sumaPLN()))
print("Wartosc portfela: " + str(portfele[1].sumaPLN()))
print("Wartosc portfela: " + str(portfele[2].sumaPLN()))
print("Wartosc portfela: " + str(portfele[3].sumaPLN()))
