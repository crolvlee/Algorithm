N, M = map(int, input().split()) # N: 표의 크기, M: 구해야하는 횟수

table = []
xy_range = []

for _ in range(N):
    line = list(map(int, input().split()))
    table.append(line)
    
for _ in range(M):
    range_line = list(map(int, input().split()))
    xy_range.append(range_line)
    
# dp 테이블 만들기
dp = [[0] * (N+1)]

# 행 슬라이싱
for line in table:
    dp_row = [0] + [line[0]]
    for num in line[1:]:
        dp_row.append(dp_row[-1] + num)
    dp.append(dp_row)
    
# 열 슬라이싱
for i in range(1, N+1):
    for j in range(N+1):
        dp[i][j] += dp[i-1][j]
        

# 게산
for range_line in xy_range:
    x1 = range_line[0]
    y1 = range_line[1]
    x2 = range_line[2]
    y2 = range_line[3]
    
    result = dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]
    print(result)