# 평범한 배낭

# N: 물품의 수, K: 준서가 버틸 수 있는 무게
N, K = map(int, input().split())
lst = [[0, 0]]

for _ in range(N):
    W, V = map(int, input().split())    # W: 물건의 무게, V: 물건의 가치
    lst.append([W, V])

# dp테이블: 최대 버틸 수 있는 무게가 i라면, 그 때의 최대 가치는 몇인지
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = lst[i][0], lst[i][1]

    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])
            
    
print(dp[N][K])