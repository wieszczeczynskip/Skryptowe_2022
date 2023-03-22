import math

season = "Zima"

def seasonChange(newSeason):
    season = newSeason
    print(season)
    def isStorm(storm):
        nonlocal season
        if storm:
            season = "Burza"
        print(season)
    isStorm(True)
    print(season)

print(season)
seasonChange("Lato")
print(season)

def circleArea(radius):
    return 2*radius*math.pi

radius = 5
print(circleArea(radius))


