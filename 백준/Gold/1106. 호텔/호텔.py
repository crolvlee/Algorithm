C, N = map(int, input().split())
cost_list = []
dp = [1e9 for _ in range(C+100)]
dp[0] = 0

for _ in range(N):
    cost, people_cnt = map(int, input().split())
    cost_list.append([cost, people_cnt])
    
for cost, people_cnt in cost_list:
    for i in range(people_cnt, C + 100):
        dp[i] = min(dp[i-people_cnt] + cost, dp[i])
        
print(min(dp[C:]))