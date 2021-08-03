# n = 입력받을 정수의 개수
# m = 숫자를 더하는 총 횟수
# k = 연속으로 더할수 있는 최대 횟수
n, m, k = map(int, input().split())
# 주어진 숫자 리스트
data = list(map(int, input().split()))

def Solution (n, m, k, data):
    answer = 0

    data.sort()
    first_number = data.pop()
    second_number = data.pop()

    count = k * (k + 1 // m)
    count += (k + 1 * k) % m

    answer += count * first_number
    answer += (m - count) * second_number

    return answer

print(Solution(n, m, k, data))