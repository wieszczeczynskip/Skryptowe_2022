import random

tura1 = 0
tura2 = 0

print("Tura 1")
temp = random.randint(1,6)
print(temp)
tura1 += temp
temp = random.randint(1,6)
print(temp)
tura1 += temp
temp = random.randint(1,6)
print(temp)
tura1 += temp
temp = random.randint(1,6)
print(temp)
tura1 += temp
print("Wynik 1 tury: " + str(tura1))

print("Tura 2")
temp = random.randint(1,6)
print(temp)
tura2 += temp
temp = random.randint(1,6)
print(temp)
tura2 += temp
temp = random.randint(1,6)
print(temp)
tura2 += temp
temp = random.randint(1,6)
print(temp)
tura2 += temp
print("Wynik 2 tury: " + str(tura2))

if (tura1 == tura2):
    print("W obu turach wyrzucono taką samą liczbę oczek - " + str(tura1))
else:
    if (tura1 > tura2):
        print("Więcej oczek wyrzucono w 1 turze - " + str(tura1))
    else:
        print("Więcej oczek wyrzucono w 2 turze - " + str(tura2))