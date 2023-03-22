import math

numbers = [19, 3, 15, 43, 98, 16, 9, 23, 4]
firsts = []
for i in numbers:
    if i == 0 or i == 1:
        continue
    first = True
    limit = math.sqrt(i)
    counter = 2
    while counter <= limit:
        if i%counter == 0:
            first = False
            print("Number " + str(i) + " is not prime. Divisors: ", end="")
            divisors = []
            for x in range(2,i):
                if i%x == 0:
                    divisors.append(x)
            print(divisors)
            break
        else:
            counter += 1
    if first:
        print("Number " + str(i) + " is prime.")
        firsts.append(i)
print(firsts)

print()

print(numbers)
numbersIncr = numbers.copy()
numbersIncr.sort()
print(numbersIncr)
numbersDecr = numbers.copy()
numbersDecr.sort()
numbersDecr.reverse()
print(numbersDecr)

print()

first3 = [numbers[0], numbers[1], numbers[2]]
numbers.remove(numbers[0])
numbers.remove(numbers[0])
numbers.remove(numbers[0])
first3.sort()
first3.extend(numbers)

print(first3)