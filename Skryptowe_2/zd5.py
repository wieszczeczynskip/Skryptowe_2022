import random

kolory = ["karo", "trefl", "pik", "kier"]
figury = ["as", "król", "dama", "joker", "10", "9"]
talia = []

for f in figury:
    for k in kolory:
        talia.append((f, k))

print(talia)
random.shuffle(talia)
print(talia)

Gracz_1 = []
Gracz_2 = []

while(len(Gracz_1) < 5):
    Gracz_1.append(talia.pop(0))
    Gracz_2.append(talia.pop(0))

print(Gracz_1)
print(Gracz_2)



print("Część druga:")

stol = []
moce = {"as": 14, "król": 13, "dama": 12, "joker": 11, "10": 10, "9": 9}
talia = []
for f in figury:
    for k in kolory:
        talia.append((f, k))
print(talia)
random.shuffle(talia)
print(talia)
Gracz_1 = []
Gracz_2 = []
while(len(talia) > 0):
    Gracz_1.append(talia.pop(0))
    Gracz_2.append(talia.pop(0))
print(Gracz_1)
print(Gracz_2)
print("Przed grą:")
print("Gracz_1: " + str(len(Gracz_1)) + " kart")
print("Gracz_2: " + str(len(Gracz_2)) + " kart")

while(len(Gracz_1) > 0 and len(Gracz_2) > 0):
    stol.append(Gracz_1.pop(0))
    stol.append(Gracz_2.pop(0))
    if(moce[stol[0][0]] > moce[stol[1][0]]):
        Gracz_1.append(stol.pop(0))
        Gracz_1.append(stol.pop(0))
    else:
        if(moce[stol[0][0]] < moce[stol[1][0]]):
            Gracz_2.append(stol.pop(0))
            Gracz_2.append(stol.pop(0))
        else:
            Gracz_1.append(stol.pop(0))
            Gracz_2.append(stol.pop(0))
print("Po grze:")
print("Gracz_1: " + str(len(Gracz_1)) + " kart")
print("Gracz_2: " + str(len(Gracz_2)) + " kart")
if(len(Gracz_1) == 0):
    print("Zwyciężył Gracz_2!")
else:
    print("Zwyciężył Gracz_1!")