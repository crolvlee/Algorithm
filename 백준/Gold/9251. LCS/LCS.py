first = input()
second = input()

dp = [[0] * (len(first) + 1) for _ in range(len(second) + 1)] 

for j in range(1, len(second) + 1):
    for i in range(1, len(first) + 1):
        if first[i-1] == second[j-1]:
            dp[j][i] = dp[j-1][i-1] + 1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp[-1][-1])