from collections import Counter
import sys

N = sys.stdin.readline()
n = list(map(int, sys.stdin.readline().split()))

M = sys.stdin.readline()
m = list(map(int,sys.stdin.readline().split()))
counter_n = Counter(n)

for i in m:
    frequency = counter_n[i]
    print(frequency)
