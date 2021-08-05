# 구구단의 모든 결과를 리스트에 담기 (리스트 내포, List comprehension)

result = [x * y for x in range(2, 10)
          for y in range(1, 10)]

print(result)