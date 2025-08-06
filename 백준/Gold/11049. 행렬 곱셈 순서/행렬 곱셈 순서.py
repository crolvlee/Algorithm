N = int(input())
A = []

for _ in range(N):
    u, v = map(int, input().split())
    A.append([u, v])

dp = [[0] * N for _ in range(N)]

# d = 간격
for d in range(1, N):
    for start in range(0, N-d):
        end = start + d
        dp[start][end] = 1e9
        
        for mid in range(start, end):
            cost = dp[start][mid] + dp[mid + 1][end] + (A[start][0] * A[mid][1] * A[end][1])
            dp[start][end] = min(dp[start][end], cost)
            
print(dp[0][N-1])