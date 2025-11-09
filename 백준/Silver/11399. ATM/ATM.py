N = int(input().strip())
P = list(map(int,input().split()))

P.sort()
num = 0
result = 0

for n in P:
  num += n
  result += num
print(result)
