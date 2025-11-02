import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

#1
print(round(sum(nums)/N))

#2
nums.sort()
print(nums[N//2])

#3
c_n = dict()
for i in nums:
    if i in c_n:
        c_n[i] += 1
    else:
        c_n[i] = 1

mx = max(c_n.values())
mx_list = []

for i in c_n:
    if c_n[i] == mx:
        mx_list.append(i)

# 두 번째로 작은 값을 출력
print(mx_list[0]) if len(mx_list) == 1 else print(mx_list[1])
    
# 4. 범위
print(max(nums)-min(nums))



