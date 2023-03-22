all_cases = []


class Loader:
    def __init__(self):
        with open("Covid.txt", encoding="utf-8") as f:
            read_data = f.read()
        f.close()
        read_data = read_data.splitlines()
        for x in range(0, len(read_data)):
            read_data[x] = read_data[x].split("\t")
        for x in read_data:
            all_cases.append(
                (x[6], int(x[3]), int(x[2]), int(x[1]), int(x[5]), int(x[4]))
            )

    def getData(self, isZgony, year, day, month, country):
        counter = 0
        if isZgony:
            for x in range(len(all_cases)):
                if (
                    all_cases[x][1] == year
                    and all_cases[x][2] == month
                    and all_cases[x][3] == day
                    and all_cases[x][0] == country
                ):
                    counter = counter + all_cases[x][4]
                    continue
            return counter
        else:
            for x in range(len(all_cases)):
                if (
                    all_cases[x][1] == year
                    and all_cases[x][2] == month
                    and all_cases[x][3] == day
                    and all_cases[x][0] == country
                ):
                    counter = counter + all_cases[x][5]
                    continue
            return counter
