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

    while m >= 0:
        for i in range(k):
            if m == 0:
                break
            answer += first_number
            m -= 1;
        if m == 0:
            break
        answer += second_number
        m -= 1;
    return answer

print(Solution(n, m, k, data))