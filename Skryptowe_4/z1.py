class Potwor:
    count = 0

    def __init__(self, zycie, sila, predkosc):
        self.zycie = zycie
        self.sila = sila
        self.predkosc = predkosc
        self.level = 1
        Potwor.count += 1

    def __repr__(self):
        return f'Mam {self.zycie} zycia, {self.sila} sily i {self.predkosc} predkosci'

    def sayHi(self):
        print(self.__class__.__name__ + " says hi")

    @classmethod
    def __len__(cls):
        return cls.count


class Zwierze(Potwor):

    def __init__(self, zycie, sila, predkosc, siersc):
        super().__init__(zycie, sila, predkosc)
        self.siersc = siersc
        self.level = 2

    def sayHi(self):
        print(self.__class__.__name__ + " mowi czesc")


class Zywiolak(Potwor):

    def __init__(self, zycie, sila, predkosc, zywiol):
        super().__init__(zycie, sila, predkosc)
        self.zywiol = zywiol

    def sayHi(self):
        super().sayHi()
        print(self.__class__.__name__ + " waves")

class Czlowiek(Potwor):

    def __init__(self, zycie, sila, predkosc, specjalnosc):
        super().__init__(zycie, sila, predkosc)
        self.specjalnosc = specjalnosc


class Golem(Potwor):

    def __init__(self, zycie, sila, predkosc, metal):
        super().__init__(zycie, sila, predkosc)
        self.metal = metal


class Dziecko(Czlowiek):

    def __init__(self, zycie, sila, predkosc, specjalnosc, wiek):
        super().__init__(zycie, sila, predkosc, specjalnosc)
        self.wiek = wiek


class Zwierzatko(Zwierze):

    def __init__(self, zycie, sila, predkosc, siersc, wiek):
        super().__init__(zycie, sila, predkosc, siersc)
        self.wiek = wiek
        self.level = 3


class Starzec(Czlowiek):

    def __init__(self, zycie, sila, predkosc, specjalnosc, zabojstwa):
        super().__init__(zycie, sila, predkosc, specjalnosc)
        self.zabojstwa = zabojstwa


golem = Golem(16, 41, 19, "stal")
lucznik = Czlowiek(34, 24, 49, "lucznik")
zywiolak = Zywiolak(1, 48, 27, "woda")
pantera = Zwierze(34, 45, 27, "jasna")
potwor = Potwor(32, 27, 25)
dziecko = Dziecko(8, 21, 49, "zabojca", 1)
starzec = Starzec(21, 33, 37, "ninja", 1)
panterka = Zwierzatko(10, 13, 48, "ciemna", 1)

print(Golem.mro())
print(Czlowiek.mro())
print(Zywiolak.mro())
print(Zwierze.mro())
print(Potwor.mro())
print(Starzec.mro())
print(Zwierzatko.mro())
print(Dziecko.mro())

golem.sayHi()
lucznik.sayHi()
zywiolak.sayHi()
pantera.sayHi()
potwor.sayHi()
dziecko.sayHi()
starzec.sayHi()
panterka.sayHi()

print(potwor.level)
print(pantera.level)
print(panterka.level)

print(f"ilość potworów: {Potwor.__len__()}")

print(golem)
print(lucznik)
print(zywiolak)
print(pantera)
print(potwor)
print(dziecko)
print(starzec)
print(panterka)