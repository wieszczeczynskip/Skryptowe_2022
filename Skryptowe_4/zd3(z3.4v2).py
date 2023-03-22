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


class GAME:

    def __init__(self, *args):
        self._wiedzma = Potwor("wiedzma", 40, 3, 200, 10)
        self._lucznik = Potwor("lucznik", 25, 5, 20, 25)
        self._pantera = Potwor("pantera", 3, 10, 10, 30)
        self._golem = Potwor("golem", 5, 1, 90, 100)
        self._level = args[0]

    @property
    def golem(self):
        return self._golem

    @property
    def pantera(self):
        return self._pantera

    @property
    def lucznik(self):
        return self._lucznik

    @property
    def wiedzma(self):
        return self._wiedzma

    @property
    def level(self):
        return self._level

    @golem.setter
    def golem(self, x):
        if isinstance(x, Potwor):
            self._golem = x
        else:
            raise ValueError('Podany atrybut to nie potwór')

    @pantera.setter
    def pantera(self, x):
        if isinstance(x, Potwor):
            self._pantera = x
        else:
            raise ValueError('Podany atrybut to nie potwór')

    @lucznik.setter
    def lucznik(self, x):
        if isinstance(x, Potwor):
            self._lucznik = x
        else:
            raise ValueError('Podany atrybut to nie potwór')

    @wiedzma.setter
    def wiedzma(self, x):
        if isinstance(x, Potwor):
            self._wiedzma = x
        else:
            raise ValueError('Podany atrybut to nie potwór')

    @golem.deleter
    def golem(self):
        del self._golem

    @pantera.deleter
    def pantera(self):
        del self._pantera

    @lucznik.deleter
    def lucznik(self):
        del self._lucznik

    @wiedzma.deleter
    def wiedzma(self):
        del self._wiedzma

    def lvlUp(self):
        self._level += 1

    def fight(self, p1, p2):
        if isinstance(p1, Potwor) and isinstance(p2, Potwor):
            p1.zycie -= p2.sila
            p2.zycie -= p1.sila
            print(p1.imie + " zaatakowal " + p2.imie + " i zadal " + str(p1.sila) + " obrazen")
            print(p2.imie + " zaatakowal " + p1.imie + " i zadal " + str(p2.sila) + " obrazen")
            if p1.zycie <= 0:
                print(p1.imie + " zginal")
                del p1
                Potwor.ilosc -= 1
                self.lvlUp()
            if p2.zycie <= 0:
                print(p2.imie + " zginal")
                del p2
                Potwor.ilosc -= 1
                self.lvlUp()
        else:
            raise ValueError("Tylko potwory mogą walczyc")

    def showLvl(self):
        print("Poziom: " + str(self.level))


# golem = Potwor("golem", 5, 1, 90, 100)
# pantera = Potwor("pantera", 3, 10, 10, 30)
# lucznik = Potwor("lucznik", 25, 5, 20, 25)
#
# golem.atak(lucznik)
# golem.ruch("wschod")
# golem.ktoStarszy(pantera)
# print("===========================")
# pantera.atak(golem)
# pantera.ruch("poludnie")
# pantera.ktoStarszy(lucznik)
# print("===========================")
# lucznik.atak(pantera)
# lucznik.ruch("polnoc")
# lucznik.ktoStarszy(golem)
# print("===========================")
# golem.atak(lucznik)
# golem.atak(lucznik)
# golem.atak(lucznik)
# golem.atak(lucznik)

game = GAME(5)
game.showLvl()
game.fight(game.pantera, game.wiedzma)
game.showLvl()

game.wiedzma = Potwor("wiedzma2",1,1,1,1)
del game.golem