import random

class ZaMalaLiczba(Exception):
    pass


def generateRandomSet():
    try:
        setLen = int(input("Podaj długość zbioru: "))
        setRange = int(input("Podaj jaka może być największa liczba: "))
        liczby = set()
        if setLen <= 0 or setRange <= 0:
            raise ZaMalaLiczba("Musisz podać liczbę większą od 0")
        while(len(liczby) < setLen):
            liczby.add(random.randint(1,setRange))
        print(liczby)
    except ValueError as e:
        print("Musisz podać liczbę całkowitą. ", e)
    except ZaMalaLiczba as e:
        print(e)

generateRandomSet()