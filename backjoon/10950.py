t = int(input())
sum = []
for i in range(t):
    a, b = map(int, input().split())
    sum.append(a + b)

for answer in sum:
    print(answer)
