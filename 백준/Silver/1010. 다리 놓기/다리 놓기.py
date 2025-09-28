import sys
import math

t = int(input())
result = []
for _ in range(t):
    n,m = map(int, input().split())
    comb=math.comb(m,n)
    result.append(comb)

for i in range(t):
    print(result[i])
  