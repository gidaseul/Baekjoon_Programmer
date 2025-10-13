t = int(input())
dp = [(1, 0), (0, 1)]  # fib(0), fib(1) 각각의 (0호출, 1호출)

# 40까지 미리 구해놓기
for i in range(2, 41):
    zero = dp[i-1][0] + dp[i-2][0]
    one = dp[i-1][1] + dp[i-2][1]
    dp.append((zero, one))

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])
