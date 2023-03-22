class Portfel:

    def __init__(self, zlote, euro, dolary):
        self.zlote = zlote
        self.euro = euro
        self.dolary = dolary

    @property
    def zlote(self):
        return self._zlote

    @property
    def euro(self):
        return self._euro

    @property
    def dolary(self):
        return self._dolary

    def printPortfel(self):
        print(f'Ilosc zlotych: {self.zlote}')
        print(f'Ilosc dolarow: {self.dolary}')
        print(f'Ilosc euro: {self.euro}')

    def sumaPLN(self):
        return self.zlote + 4.75 * self.euro + 4.3 * self.dolary

    @zlote.setter
    def zlote(self, x):
        if isinstance(x, (int, float)):
            if x > 0:
                self._zlote = x
            else:
                raise ValueError('This attribute must be positive.')
        else:
            raise TypeError('This attribute must be an int or float value.')

    @euro.setter
    def euro(self, x):
        if isinstance(x, (int, float)):
            if x > 0:
                self._euro = x
            else:
                raise ValueError('This attribute must be positive.')
        else:
            raise TypeError('This attribute must be an int or float value.')

    @dolary.setter
    def dolary(self, x):
        if isinstance(x, (int, float)):
            if x > 0:
                self._dolary = x
            else:
                raise ValueError('This attribute must be positive.')
        else:
            raise TypeError('This attribute must be an int or float value.')

    @zlote.deleter
    def zlote(self):
        del self._zlote

    @euro.deleter
    def euro(self):
        del self._euro

    @dolary.deleter
    def dolary(self):
        del self._dolary



portfele = []
portfele.append(Portfel(1,1,1))
portfele.append(Portfel(1,1,1))
portfele.append(Portfel(1,1,1))
portfele.append(Portfel(1,1,1))
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
# portfele[3].zlote = "999"
for x in portfele:
    x.printPortfel()
print("===========================")
print("Wartosc portfela: " + str(portfele[0].sumaPLN()))
print("Wartosc portfela: " + str(portfele[1].sumaPLN()))
print("Wartosc portfela: " + str(portfele[2].sumaPLN()))
print("Wartosc portfela: " + str(portfele[3].sumaPLN()))
portfele[3].zlote = 500
del portfele[3].dolary