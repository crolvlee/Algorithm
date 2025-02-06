import heapq
INF = 1e9

# (0, 0)에서 (N-1, M-1)로 가는 걸로 하겠음

M, N = map(int, input().split())
ground = []

for i in range(N):
    line = list(map(int, input().strip()))
    ground.append(line)


distance = [[INF] * M for _ in range(N)]

def dijkstra(start_row, start_col):
    q = []
    
    heapq.heappush(q, [0, start_row, start_col])    # [거리, 시작 행, 시작 열]
    distance[start_row][start_col] = 0
    
    while q:
        dist, now_row, now_col = heapq.heappop(q)
        
        # 앞에서 거리 업데이트 된게 지금 거리보다 작으면 -> 지금 거리 필요 없음
        if distance[now_row][now_col] < dist:
            continue
        
        # 오른쪽 노드
        if now_col + 1 <= M - 1:
            cost_right = dist + ground[now_row][now_col + 1]
            if cost_right < distance[now_row][now_col + 1]:
                distance[now_row][now_col + 1] = cost_right
                heapq.heappush(q, [cost_right, now_row, now_col + 1])
                
        # 왼쪽 노드
        if now_col - 1 >= 0:
            cost_left = dist + ground[now_row][now_col - 1]
            if cost_left < distance[now_row][now_col - 1]:
                distance[now_row][now_col - 1] = cost_left
                heapq.heappush(q, [cost_left, now_row, now_col - 1])
        
        # 아랫쪽 노드
        if now_row + 1 <= N - 1:
            cost_down = dist + ground[now_row + 1][now_col]
            if cost_down < distance[now_row + 1][now_col]:
                distance[now_row + 1][now_col] = cost_down
                heapq.heappush(q, [cost_down, now_row + 1, now_col])
                
        # 윗쪽 노드
        if now_row - 1 >= 0:
            cost_up = dist + ground[now_row - 1][now_col]
            if cost_up < distance[now_row - 1][now_col]:
                distance[now_row - 1][now_col] = cost_up
                heapq.heappush(q, [cost_up, now_row - 1, now_col])

dijkstra(0, 0)
print(distance[N-1][M-1])
