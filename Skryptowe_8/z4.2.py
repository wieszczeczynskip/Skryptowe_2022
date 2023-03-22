import z2, z3, z4

class Person:

    def __init__(self, name, lname, number):
        if isinstance(name, z2.First_name):
            self.name = name
        if isinstance(lname, z3.Last_name):
            self.lname = lname
        if isinstance(number, z4.Ident_number):
            self.number = number

    def fromString(self, string):
        if string.count(" ") != 0:
            string = string.split(" ")
        if string.count(";") != 0:
            string = string.split(";")
        if string.count("/") != 0:
            string = string.split("/")
        if len(string) == 3:
            self.name = z2.First_name(string[0])
            self.lname = z3.Last_name(string[1])
            self.number = z4.Ident_number(string[2])

fn = z2.First_name("Alan")
ln = z3.Last_name("Nowak")
nb = z4.Ident_number("123456728")
prs = Person(fn, ln, nb)

print("z5")
print(prs.name)
print(prs.lname)
print(prs.number)

prs.fromString("Dawid;Kowalski;143456730")

print(prs.name)
print(prs.lname)
print(prs.number)
