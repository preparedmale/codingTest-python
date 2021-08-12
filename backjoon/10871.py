import sys

n, x = map(int, sys.stdin.readline().split())
a = map(int, sys.stdin.readline().split())

for number in a:
    if number < x:
        print(number, end=' ')

