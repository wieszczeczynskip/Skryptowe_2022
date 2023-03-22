import z1


class Last_name(z1.Controlled_text):
    def __init__(self, lname):
        super().__init__(lname)
        self.lname = lname

    @property
    def lname(self):
        return self._lname

    @lname.setter
    def lname(self, newLname):
        if newLname.count("-") == 1:
            newLnameSplit = newLname.split("-")
            if (
                newLnameSplit[0] == newLnameSplit[0].capitalize()
                and str.isalpha(newLnameSplit[0])
                and newLnameSplit[1] == newLnameSplit[1].capitalize()
                and str.isalpha(newLnameSplit[1])
            ):
                self._lname = newLname
            else:
                raise Exception("Złe nazwisko")
        else:
            if str.isalpha(newLname) and newLname == newLname.capitalize():
                self._lname = newLname
            else:
                raise Exception("Złe nazwisko")

    @lname.deleter
    def lname(self):
        del self._lname


print("z3")
ln1 = Last_name("Nowak")
print(ln1.lname)
# ln1.lname = "kowalski"
# ln1.lname = "nowak-kowalski"
ln1.lname = "Nowak-Kowalski"
print(ln1.lname)