x = int(input())
y = int(input())

print(x * (y % 10))
print(x * (y % 100 - y % 10) // 10)
print(x * (y - y % 100) // 100)
print(x * y)