import random

countries = ['Uruguay','Russia','Saudi Arabia','Egypt','Spain','Portugal', 'Iran','Morocco', 'France','Denmark','Peru',
             'Australia', 'Croatia','Argentina', 'Nigeria', 'Iceland','Brazil', 'Switzerland', 'Serbia', 'Costa Rica',
             'Sweden','Mexico', 'Korea Republic', 'Germany', 'Belgium','England', 'Tunisia', 'Panama','Colombia',
             'Japan', 'Senegal', 'Poland']

print(countries)

random.shuffle(countries)

print(countries)

A = []
B = []
C = []
D = []
E = []
F = []
G = []
H = []

A.append(countries[random.randint(0, len(countries)-1)])
B.append(countries[random.randint(0, len(countries)-1)])
C.append(countries[random.randint(0, len(countries)-1)])
D.append(countries[random.randint(0, len(countries)-1)])
E.append(countries[random.randint(0, len(countries)-1)])
F.append(countries[random.randint(0, len(countries)-1)])
G.append(countries[random.randint(0, len(countries)-1)])
H.append(countries[random.randint(0, len(countries)-1)])

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)