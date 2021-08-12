import sys

answer =[]

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())
        answer.append(a + b)
    except:
        break

answer.reverse()
while answer:
    print(answer.pop())
