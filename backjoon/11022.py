import sys
t = int(sys.stdin.readline())

answer = []

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    answer.append([a, b, a + b])

for i in range(t):
    print('Case #{0}: {1} + {2} = {3}'.format(i + 1, answer[i][0], answer[i][1], answer[i][2]))


