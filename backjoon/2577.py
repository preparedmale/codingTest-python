import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = str(a * b * c)

for i in range(0, 10):
    print(result.count(str(i)))
