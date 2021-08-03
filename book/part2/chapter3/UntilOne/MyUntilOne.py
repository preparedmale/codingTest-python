# inputValue N: Number that should be 1 K: Operand of division

# 1. Receive input values
n, k = map(int, input().split())

def Solution(n, k):
    answer = 0

    while n != 1:
        if n % k != 0:
            n -= 1
            print(n)
            answer += 1
            continue
        n //= k
        print(n)
        answer += 1

    return answer

print(Solution(n, k))