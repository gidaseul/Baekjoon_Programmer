import sys

input = sys.stdin.readline

N,X = map(int,input().split())
visits = list(map(int, input().split()))

window_sum = sum(visits[:X])
max_sum = window_sum
count = 1

for i in range(X,N):
    window_sum += visits[i] - visits[i - X]  # 슬라이딩 하면서 빠지는 값, 더해지는 값을 이용하여 시간 개선

    if window_sum > max_sum:
        max_sum = window_sum
        count = 1
    elif window_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)


