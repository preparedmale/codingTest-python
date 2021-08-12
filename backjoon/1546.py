import sys

subjects_count = int(sys.stdin.readline())

scores = list(map(int, sys.stdin.readline().split()))
high_score = max(scores)
sum = 0

while scores:
    sum += (scores.pop() / high_score) * 100
answer = sum / subjects_count

print(answer)
