import sys

t = int(sys.stdin.readline())

results = []
answers = []
for i in range(t):
    results.append(sys.stdin.readline())

for result in results:
    sum = 0
    con = 0
    for i in range(len(result)):
        if result[i] == 'O':
            con += 1
            sum += con
        else:
            con = 0
    answers.append(sum)

answers.reverse()
while answers:
    print(answers.pop())


