class Potwor:

    def __init__(self, zycie, sila, predkosc):
        self.zycie = zycie
        self.sila = sila
        self.predkosc = predkosc

    def __repr__(self):
        return f'Mam {self.zycie} zycia, {self.sila} sily i {self.predkosc} predkosci'

class Zwierze(Potwor):

    def __init__(self, *args, **kwargs):
        super().__init__(sum(*args), kwargs.get("sila", 0), kwargs.get("predkosc", 0))
        self.siersc = kwargs.get("siersc")


class Zywiolak(Potwor):

    def __init__(self, *args, **kwargs):
        super().__init__(sum(*args), kwargs.get("sila", 0), kwargs.get("predkosc", 0))
        self.zywiol = kwargs.get("zywiol")


class Czlowiek(Potwor):

    def __init__(self, *args, **kwargs):
        super().__init__(sum(*args), kwargs.get("sila", 0), kwargs.get("predkosc", 0))
        self.specjalnosc = kwargs.get("specjalnosc")
        self.wiek = kwargs.get("wiek")


class Golem(Potwor):

    def __init__(self, *args, **kwargs):
        super().__init__(sum(*args), kwargs.get("sila", 0), kwargs.get("predkosc", 0))
        self.metal = kwargs.get("metal")


golem = Golem([16, 26, 70], sila=41, predkosc=19, metal="stal")
lucznik = Czlowiek([34], sila=24, predkosc=49, specjalnosc="lucznik", zyje=False)
zywiolak = Zywiolak([1], predkosc=27, zywiol="woda")
pantera = Zwierze([34], sila=45, predkosc=27, siersc="jasna")
potwor = Potwor(32, 27, 25)

print(golem)
print(lucznik)
print(zywiolak)
print(pantera)
print(potwor)
