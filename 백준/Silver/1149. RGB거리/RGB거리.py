# RGB 거리

# 0.5초 -> 연산 횟수 최대 5000만 
# O(N)   : N이 최대 5000만
# O(N^2) : N이 7000 정도?

# 각각의 집은 R, G, B 중 하나로 칠함
# 모든 집을 칠하는 비용의 최솟값 프린트
# 인접한 집끼리는 색이 달라야 함


N = int(input())    # 집의 개수
cost_list = []

for i in range(N):
    R, G, B = map(int, input().split())
    cost_list.append([R, G, B])
    
dp = [[0, 0, 0] for _ in range(N)]
dp[0] = cost_list[0]

for j in range(1, N):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost_list[j][0]    # 이번 턴에 R을 선택하는 경우
    dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost_list[j][1]    # 이번 턴에 G를 선택하는 경우
    dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost_list[j][2]    # 이번 턴에 B를 선택하는 경우
    
print(min(dp[-1]))