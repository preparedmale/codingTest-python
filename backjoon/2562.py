import sys

array = []
for i in range(9):
    n = int(sys.stdin.readline())

    array.append(n)

max_value = max(array)
print(max_value)
print(array.index(max_value) + 1)
