import random

class Kostki:

    tura1wynik = 0
    tura2wynik = 0

    def tura1(self):
        print("Tura 1")
        temp = random.randint(1,6)
        print(temp)
        self.tura1wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura1wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura1wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura1wynik += temp

    def tura2(self):
        print("Tura 2")
        temp = random.randint(1,6)
        print(temp)
        self.tura2wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura2wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura2wynik += temp
        temp = random.randint(1,6)
        print(temp)
        self.tura2wynik += temp

    def sprawdzWynik(self):
        if (self.tura1wynik == self.tura2wynik):
            print("W obu turach wyrzucono taką samą liczbę oczek - " + str(self.tura1wynik))
        else:
            if (self.tura1wynik > self.tura2wynik):
                print("Więcej oczek wyrzucono w 1 turze - " + str(self.tura1wynik))
            else:
                print("Więcej oczek wyrzucono w 2 turze - " + str(self.tura2wynik))

    def resetWynik(self):
        self.tura1wynik = 0
        self.tura2wynik = 0



kostki = Kostki()
kostki.tura1()
kostki.tura2()
kostki.sprawdzWynik()
kostki.resetWynik()
kostki.sprawdzWynik()