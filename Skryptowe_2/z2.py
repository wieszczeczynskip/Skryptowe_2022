def sum(*args):
    global outcome
    outcome = 0
    print(args)
    for x in args:
        print(x)
        outcome = outcome + x


sum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(outcome)


def light(day, **kwargs):
    fog = False
    rain = False
    snow = False
    fog = kwargs.get("fog")
    rain = kwargs.get("rain")
    snow = kwargs.get("snow")
    if (fog or snow or rain):
        print("Światło będzie włączone")
    else:
        print("Światło będzie wyłączone")


day = True
light(day, rain=True)
