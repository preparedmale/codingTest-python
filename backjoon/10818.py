import sys

n = map(int, sys.stdin.readline())
numbers = []

numbers = list(map(int, sys.stdin.readline().split()))

numbers.sort()

max_number = numbers[-1]
min_number = numbers[0]

print(min_number, max_number)

