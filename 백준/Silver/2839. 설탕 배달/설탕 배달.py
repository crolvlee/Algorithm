N = int(input())
dp = [-1] * (5001)
dp[3] = 1
dp[4] = -1
dp[5] = 1
dp[6] = 2
dp[7] = -1

for i in range(8, 5000+1):
    prev_3 = dp[i-3]
    prev_5 = dp[i-5]
    
    if prev_3 != -1 and prev_5 != -1:
        dp[i] = min(prev_3 + 1, prev_5 + 1)
    elif prev_3 == -1 and prev_5 != -1:
        dp[i] = prev_5 + 1
    elif prev_3 != -1 and prev_5 == -1:
        dp[i] = prev_3 + 1
        
print(dp[N])