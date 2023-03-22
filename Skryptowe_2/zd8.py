import time
import os

pies = "Buldog"
pieski = ["Mops", "Owczarek", "Golden", "Szpic", "Husky"]

strona = input("Podaj swoją ulubioną stronę internetową: ")

filename = "C:\\Users\\szawe\\PycharmProjects\\Skryptowe_2\\txt.txt"

file = open(filename, 'r')
content = file.read()
print(content)
file.close()

with open(filename, 'a') as file:
    file.write(strona)
    file.write(pies)
    file.write('\n')
    file.writelines(pieski)
    for piesek in pieski:
        file.write(piesek+'\n')