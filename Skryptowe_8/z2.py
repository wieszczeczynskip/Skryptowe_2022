import z1


class First_name(z1.Controlled_text):
    names = []

    def __init__(self, name):
        super().__init__(name)
        if len(self.names) == 0:
            self.loadNames()
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newName):
        newName = newName.capitalize()
        if newName in First_name.names:
            self._name = newName
        else:
            raise Exception("Nieprawidłowe imie")

    @name.deleter
    def name(self):
        del self._name

    @classmethod
    def loadNames(cls):
        try:
            with open("PopularneImiona.txt", encoding="utf-8") as f:
                for x in f:
                    x = x.strip()
                    if x != "Kobiety" and x != "Mężczyźni":
                        cls.names.append(x)
        except IOError:
            raise Exception("Błąd pliku")

    @classmethod
    def ismale(cls, name):
        if name[len(name) - 1] == "a":
            return False
        return True

    @classmethod
    def isfemale(cls, name):
        return not cls.ismale(name)


print("z2")
fn1 = First_name("alan")
First_name.loadNames()
print(fn1.ismale("alan"))
print(fn1.isfemale("hanna"))
print(fn1.name)
fn1.name = "hanna"
print(fn1.name)
