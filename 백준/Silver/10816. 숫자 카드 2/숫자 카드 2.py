from collections import Counter
import sys

N = sys.stdin.readline()
n = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()
m = list(map(int, sys.stdin.readline().split()))

counter_n = Counter(n)

result = []  # 결과를 저장할 리스트

for i in m:
    frequency = counter_n[i]
    result.append(frequency)  # 빈도수를 리스트에 추가

print(*result)  # 리스트의 요소들을 공백으로 구분하여 출력