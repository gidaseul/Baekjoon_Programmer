def num_residents_optimized(k,n):
    dp = [i for i in range(1, n+1)]


    for _ in range(k):
        for j in range(1,n):
            dp[j] += dp[j-1]
    
    return dp[n-1]
    
t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(num_residents_optimized(k, n))
