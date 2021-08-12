import sys
t = int(sys.stdin.readline())

answer = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())

    answer.append(a + b)

for a in answer:
    print(a)



