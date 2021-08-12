import sys

c = int(sys.stdin.readline())
cases = []
answers = []

for _ in range(c):
    cases.append(list(map(int, sys.stdin.readline().split())))

for case in cases:
    student_count = case[0]
    score_sum = 0
    score_avg = 0
    success_students_count = 0
    for i in range(1, student_count + 1):
        score_sum += case[i]
    score_avg = score_sum / student_count
    for i in range(1, student_count + 1):
        if score_avg < case[i]:
            success_students_count += 1
    answers.append((success_students_count / student_count) * 100)

answers.reverse()
while answers:
    print("{0:0.3f}%".format(answers.pop()))

