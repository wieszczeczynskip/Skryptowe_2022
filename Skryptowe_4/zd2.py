import time

def timer(func):
    def wraper(n):
        print("Czas wykonywania funkcji[ns]: ")
        time1 = time.time_ns()
        func(n)
        print(time.time_ns() - time1)
    return wraper

@timer
def silnia(n):
    s = 1
    for i in range(2, n + 1):
        s *= i
    return s

silnia(100000)
