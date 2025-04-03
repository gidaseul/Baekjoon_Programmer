import sys

N,X = map(int, sys.stdin.readline().split())

d = list(map(int, sys.stdin.readline().split()))

if len(d) < 2:
    print(0)
else:
    a = float('inf')
    for i in range(len(d)-1):
        a = min(a, d[i] + d[i+1])
    print(a*X)