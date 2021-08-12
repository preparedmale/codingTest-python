import sys

answer = []

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0:
        break
    answer.append(a + b)
answer.reverse()

while answer:
    print(answer.pop())

