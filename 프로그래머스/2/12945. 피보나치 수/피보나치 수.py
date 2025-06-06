def solution(n):
    dp = [0] * 100001
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, 100001):
        dp[i] = dp[i-2] + dp[i-1]
    
    answer = dp[n] % 1234567
    return answer