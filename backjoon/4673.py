constructors = []
numbers = set(list(range(1, 10001)))

for i in range(1, 10001):
    digits = str(i)
    sum = i
    for digit in digits:
        sum += int(digit)

    constructors.append(sum)

constructors = set(constructors)

self_number = list(numbers - constructors)
self_number.sort()
self_number.reverse()

while self_number:
    print(self_number.pop())




