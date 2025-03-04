import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

s = set(arr)

M = int(input())
queries = list(map(int, input().split()))

for q in queries:
    if q in s:
        print(1)
    else:
        print(0)