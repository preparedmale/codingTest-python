# receive input values
n = int(input())
directions = input().split()

# variable initialize

# define method
def Solution(n, direction):
    answer = [1, 1]

    direction_dic = {'R' : [0, 1], 'L' : [0, -1], 'U' : [-1, 0], 'D' : [1, 0]}

    for direction in directions:
        answer[0] += direction_dic.get(direction)[0]
        answer[1] += direction_dic.get(direction)[1]
        if answer[0] > n:
            answer[0] -= 1
        elif answer[0] < 1:
            answer[0] += 1
        elif answer[1] > n:
            answer[1] -= 1
        elif answer[1] < 1:
            answer[1] += 1

    return answer

result = Solution(n, directions)

print(result[0], result[1])