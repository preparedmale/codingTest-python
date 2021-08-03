# 숫자 카드들이 놓인 행의 개수 N, 열의 갯수 M
n, m = map(int, input().split())

def Solution(n, m):
    data = []
    for _ in range(n):
        min_value = min(list(map(int, input().split())))
        data.append(min_value)
    data.sort()

    answer = data[-1]
    return answer

print(Solution(n, m))