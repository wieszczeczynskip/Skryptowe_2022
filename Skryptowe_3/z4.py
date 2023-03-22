class Potwor:
    ilosc = 0

    def __init__(self, imie, sila, predkosc, wiek, zycie):
        Potwor.ilosc += 1
        self.imie = imie
        self.sila = sila
        self.predkosc = predkosc
        self.wiek = wiek
        self.zycie = zycie

    def atak(self, przeciwnik):
        if isinstance(przeciwnik, Potwor):
            przeciwnik.zycie = przeciwnik.zycie - self.sila
            print(self.imie + " zaatakowal " + przeciwnik.imie + " i zadal " + str(self.sila) + " obrazen")
        if przeciwnik.zycie <= 0:
            print(przeciwnik.imie + " zginal")
            del przeciwnik
            Potwor.ilosc -= 1

    def ktoStarszy(self, przeciwnik):
        if isinstance(przeciwnik, Potwor):
            if (przeciwnik.wiek == self.wiek):
                print(przeciwnik.imie + " i " + self.imie + " maja tyle samo lat")
            else:
                if (przeciwnik.wiek > self.wiek):
                    print(przeciwnik.imie + " jest starszy od " + self.imie)
                else:
                    print(self.imie + "jest starszy od " + przeciwnik.imie)

    def ruch(self, kierunek):
        print("Poruszyles sie o " + str(self.predkosc) + " pol w kierunku: " + kierunek)


golem = Potwor("golem", 5, 1, 90, 100)
pantera = Potwor("pantera", 3, 10, 10, 30)
lucznik = Potwor("lucznik", 25, 5, 20, 25)

golem.atak(lucznik)
golem.ruch("wschod")
golem.ktoStarszy(pantera)
print("===========================")
pantera.atak(golem)
pantera.ruch("poludnie")
pantera.ktoStarszy(lucznik)
print("===========================")
lucznik.atak(pantera)
lucznik.ruch("polnoc")
lucznik.ktoStarszy(golem)
print("===========================")
golem.atak(lucznik)
golem.atak(lucznik)
golem.atak(lucznik)
golem.atak(lucznik)

