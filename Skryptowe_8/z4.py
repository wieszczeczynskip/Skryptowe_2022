import z1
from typing import Final

class Ident_number(z1.Controlled_text):

    def __init__(self, number):
        super().__init__(number)
        self.__number:Final = number

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, newNumber):
        if str.isnumeric(newNumber) and len(newNumber) == 9:
            check1 = int(newNumber[len(newNumber)-2:])
            check2 = 0
            for x in newNumber[:7]:
                check2+=int(x)
            if check1 == check2 % 97:
                self.__number = newNumber
            else:
                raise Exception("Zły numer kontrolny")
        else:
            raise Exception("Zły numer")

print("z4")
x = Ident_number("123456728")
print(x.number)
x.number = "123456729"
print(x.number)