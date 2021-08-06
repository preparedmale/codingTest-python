# 정수 N을 입력받는다.
n = int(input())

def Solution(n):
    answer = 0

    for h in range(n + 1):
        for m in range(60):
            for s in range(60):
                if str(h).find('3') != -1 or str(m).find('3') != -1 or str(s).find('3') != -1:
                    answer += 1

    return answer

print(Solution(n))