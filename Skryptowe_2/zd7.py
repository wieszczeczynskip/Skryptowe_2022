import time
import os

dirIsOk = False
fileIsOk = False

# C:\Users\szawe\PycharmProjects\Skryptowe_2
# txt.txt

while not dirIsOk:
    dir = input("Wprowadz ścieżkę dostępu do katalogu: ")
    if not os.path.isdir(dir):
        print("Ścieżka dostępu musi być katalogiem.")
    else:
        dirIsOk = True
        while not fileIsOk:
            file = input("Wprowadz nazwę pliku: ")
            if not os.path.isfile(file):
                print("Nie została wprowadzona nazwa pliku: ")
            else:
                fileIsOk = True
                fullpath = os.path.join(dir, file)
                print("Ostatnia modyfikacja:")
                print(time.localtime(os.path.getmtime(fullpath)))
                print("Utworzono:")
                print(time.localtime(os.path.getctime(fullpath)))
                print("Ostatni dostęp:")
                print(time.localtime(os.path.getatime(fullpath)))
                print("Rozmiar:")
                print(os.path.getsize(fullpath))