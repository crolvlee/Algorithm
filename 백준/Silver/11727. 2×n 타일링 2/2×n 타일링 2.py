n = int(input())
dp = [0, 1, 3]

for i in range(3, n+1):
    # (i-2)결과에 추가하는 것
    first = dp[i-2] * 2
    
    # (i-1)결과에 추가하는 것
    second = dp[i-1]
    
    new = first + second
    dp.append(new)
    
print(dp[n] % 10007)