import sys
import collections as col

deq = col.deque()
n = int(sys.stdin.readline())
for i in range(n):
    deq.append(i+1)

while len(deq) > 1:
    deq.popleft()
    deq.rotate(-1)

print(deq[0])