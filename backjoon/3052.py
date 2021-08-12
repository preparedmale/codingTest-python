import sys

remainders = []
for i in range(10):
    n = int(sys.stdin.readline())

    remainder = n % 42
    remainders.append(remainder)

answer = set(remainders)
print(len(answer))