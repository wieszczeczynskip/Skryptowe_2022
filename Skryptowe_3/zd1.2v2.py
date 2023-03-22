import sys

daytime = True
fog = True
rain = False
snow = False


def bikeLight():
    light = False
    try:
        if bool(int(input("Czy jest dzień? [1] Tak, [0] Nie"))):
            if bool(int(input("Czy jest mgła? [1] Tak, [0] Nie"))):
                light = True
            else:
                if bool(int(input("Czy pada śnieg? [1] Tak, [0] Nie"))):
                    light = True
                else:
                    if bool(int(input("Czy pada deszcz? [1] Tak, [0] Nie"))):
                        light = True
        else:
            light = True

        if light:
            print("The light is ON")
        else:
            print("The light is OFF")
    except ValueError as e:
        print("Musisz odpowiedzieć Tak lub Nie. ", e)
    except:
        print("Coś poszło nie tak... ", sys.exc_info()[0])

bikeLight()

