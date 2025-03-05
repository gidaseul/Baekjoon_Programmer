from collections import deque
import sys

n, k = map(int, sys.stdin.readline().split())

dq = deque(range(1, n + 1))
result = []

while dq:
    for _ in range(k - 1):
        dq.append(dq.popleft())
    result.append(dq.popleft())

# 요구되는 출력 형식에 맞춰서 결과 출력
print("<" + ", ".join(str(x) for x in result) + ">")
