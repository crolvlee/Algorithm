n = int(input())

# dp 배열
dp = [1e9] * (n+1)
dp[0] = 0
dp[1] = 1

# dp 채우기
for i in range(2, n+1):

    j = 1
    while j*j <= i:
        now_cnt = 1 + dp[i - j*j]
        dp[i] = min(dp[i], now_cnt)
        j += 1

print(dp[n])
