auto = True
switch = True
daytime = True
fog = True
rain = False
snow = False


if auto:
    if not(daytime) or fog or rain or snow:
        light = True
    else:
        light = False
else:
    if switch:
        light = True
    else:
        light = False

if light:
    print("The light is ON")
else:
    print("The light is OFF")



