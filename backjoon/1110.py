n = input()

if len(n) == 1:
    n = n.replace(n, "0{0}".format(n))

second_number = str(int(n[0]) + int(n[-1]))
first_number = n[-1]

answer = first_number + second_number
cycle = 1

while n != answer:
    second_number = str(int(answer[0]) + int(answer[-1]))
    first_number = answer[-1]

    answer = first_number + second_number[-1]
    cycle += 1

print(cycle)
