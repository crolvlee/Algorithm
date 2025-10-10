# 입력받기
N = int(input())
lst = []

for _ in range(N):
    r, c = map(int, input().split())
    lst.append([r, c])
    
# dp 배열
dp = [[0] * N for _ in range(N)]

# d = start와 end 차이
for d in range(1, N+1):
    for start in range(0, N-d):
        end = start + d
        dp[start][end] = 1e9
        
        for mid in range(start, end):
            cost = dp[start][mid] + dp[mid+1][end] + (lst[start][0] * lst[mid][1] * lst[end][1])
            dp[start][end] = min(dp[start][end], cost)
            
print(dp[0][N-1])