from timeit import default_timer as timer

def timerr(func):
    def wrapper(*args, **kwargs):
        start = timer()
        print(func(*args, **kwargs))
        end = timer():
        print((end - start) * 1000)
    return wrapper


# z1

with open("Covid.txt", encoding="utf-8") as f:
    read_data = f.read()
f.close()
read_data = read_data.splitlines()
for x in range(0, len(read_data)):
    read_data[x] = read_data[x].split("\t")
#
# def read_some_all_cases(x):
#     all_cases = []
#     match x:
#         case 6:
#             for x in read_data:
#                 all_cases.append((x[6], int(x[3]), int(x[2]), int(x[1]), int(x[5]), int(x[4])))
#         case 5:
#             for x in read_data:
#                 all_cases.append((x[6], int(x[3]), int(x[2]), int(x[1]), int(x[5])))
#         case 4:
#             for x in read_data:
#                 all_cases.append((x[6], int(x[3]), int(x[2]), int(x[1])))
#         case 3:
#             for x in read_data:
#                 all_cases.append((x[6], int(x[3]), int(x[2])))
#         case 2:
#             for x in read_data:
#                 all_cases.append((x[6], int(x[3])))
#         case 1:
#             for x in read_data:
#                 all_cases.append((x[6]))
#     return all_cases
#
# all_cases = read_some_all_cases(6)
# for x in all_cases:
#     print(x)

all_cases = []
for x in read_data:
    all_cases.append((x[6], int(x[3]), int(x[2]), int(x[1]), int(x[5]), int(x[4])))

by_date = {}
dates = set()
for x in read_data:
    dates.add(x[0])
for x in dates:
    temp = []
    dict_phrase = (1, 1, 1)
    for y in read_data:
        if x == y[0]:
            dict_phrase = ((int(y[3]), int(y[2]), int(y[1])))
            temp.append((y[6], int(y[5]), int(y[4])))
    by_date[dict_phrase] = temp

by_country = {}
countries = set()
for x in read_data:
    countries.add(x[6])
for x in countries:
    temp = []
    for y in read_data:
        if x == y[6]:
            temp.append((int(y[3]), int(y[2]), int(y[1]), int(y[5]), int(y[4])))
    by_country[x] = temp


# ================================================================================
# z2

@timerr
def for_date_a(year, month, day):
    result = (0, 0)
    for x in all_cases:
        if (x[1] == year and x[2] == month and x[3] == day):
            result = (result[0] + x[4], result[1] + x[5])
    return result

@timerr
def for_date_d(year, month, day):
    result = (0, 0)
    for x in by_date[(year, month, day)]:
        result = (result[0] + x[1], result[1] + x[2])
    return result

@timerr
def for_date_c(year, month, day):
    result = (0, 0)
    for x in by_country.values():
        for y in x:
            if (y[0] == year and y[1] == month and y[2] == day):
                result = (result[0] + y[3], result[1] + y[4])
    return result

print("Zadanie 2")
for_date_a(2020, 11, 25)
for_date_d(2020, 11, 25)
for_date_c(2020, 11, 25)

# ================================================================================
# z3

@timerr
def for_country_a(country):
    result = (0, 0)
    for x in all_cases:
        if (x[0] == country):
            result = (result[0] + x[4], result[1] + x[5])
    return result

@timerr
def for_country_d(country):
    result = (0, 0)
    for x in by_date.values():
        for y in x:
            if (y[0] == country):
                result = (result[0] + y[1], result[1] + y[2])
    return result

@timerr
def for_country_c(country):
    result = (0, 0)
    for x in by_country[country]:
        result = (result[0] + x[3], result[1] + x[4])
    return result

print("Zadanie 3")
for_country_a("Poland")
for_country_d("Poland")
for_country_c("Poland")


# ================================================================================
# z4

@timerr
def for_date_country_a(year, month, day, country):
    for x in all_cases:
        if (x[1] == year and x[2] == month and x[3] == day and x[0] == country):
            return (x[4], x[5])

@timerr
def for_date_country_d(year, month, day, country):
    for x in by_date[(year, month, day)]:
        if (x[0] == country):
            return (x[1], x[2])

@timerr
def for_date_country_c(year, month, day, country):
    for x in by_country[country]:
        if (x[0] == year and x[1] == month and x[2] == day):
            return (x[3], x[4])

print("Zadanie 4")
for_date_country_a(2020, 11, 25, "Poland")
for_date_country_d(2020, 11, 25, "Poland")
for_date_country_c(2020, 11, 25, "Poland")

