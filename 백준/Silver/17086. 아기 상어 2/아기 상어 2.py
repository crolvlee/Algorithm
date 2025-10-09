from collections import deque

# 입력받기
N, M = map(int, input().split())
ground = []

for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)
    
# BFS 함수
def BFS(start_row, start_col):
    # 동 / 서 / 남 / 북 / 동북 / 동남 / 남서 / 북서
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
    
    q = deque()
    q.append([start_row, start_col])
    dist = [[-1] * M for _ in range(N)]
    dist[start_row][start_col] = 0
    result = 0

    while True:
        now_row, now_col = q.popleft()
        if ground[now_row][now_col] == 1:
            result = dist[now_row][now_col]
            break
        
        for d_row, d_col in direction:
            next_row = now_row + d_row
            next_col = now_col + d_col
            
            if 0 <= next_row <= N-1 and 0 <= next_col <= M-1 and dist[next_row][next_col] == -1:
                dist[next_row][next_col] = dist[now_row][now_col] + 1
                q.append([next_row, next_col]) 
            
    return result

# 안전거리 배열
safe_dist = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        safe_dist[i][j] = BFS(i, j)
        
# 정답 찾기
answer = 0
for line in safe_dist:
    answer = max(answer, max(line))
    
print(answer)