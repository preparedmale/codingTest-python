import sys

n = int(sys.stdin.readline())
dif = 0
answer = 0
for number in range(1, n +1):
    number = str(number)
    number_length = len(str(number))
    isAnswer = False
    for i in range(number_length):
        if number_length == 1:
            isAnswer = True
        elif i + 1 < number_length and i == 0:
            dif = int(number[i]) - int(number[i + 1])
            isAnswer = True
        elif i + 1 < number_length:
            if dif == int(number[i]) - int(number[i + 1]):
                isAnswer = True
            else:
                isAnswer = False
                break
    if isAnswer:
        answer += 1
print(answer)

