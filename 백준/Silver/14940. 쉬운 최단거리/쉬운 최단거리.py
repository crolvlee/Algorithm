from collections import deque

# 편의상 (start_row, start_col)에서 다른 지점으로 가는 것으로 하겠음

n, m = map(int, input().split())
ground = []
start_row, start_col = -1, -1
for i in range(n):
    line = list(map(int, input().split()))
    ground.append(line)
    
    for j in range(len(line)):
        if line[j] == 2:
            start_row = i
            start_col = j

distance = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            distance[i][j] = 0

def BFS(start_row, start_col, dist):
    q = deque([])   # [[행 번호, 열 번호, start와의 거리], [], ....]
    q.append([start_row, start_col, dist])
    distance[start_row][start_col] = dist

    while q:
        now_row, now_col, now_dist = q.popleft()

        # 상
        if now_row - 1 >= 0:
            if ground[now_row - 1][now_col] == 1:
                if distance[now_row - 1][now_col] == -1:
                    distance[now_row - 1][now_col] = now_dist + 1
                    q.append([now_row - 1, now_col, now_dist + 1])

        # 하
        if now_row + 1 <= n-1:
            if ground[now_row + 1][now_col] == 1:
                if distance[now_row + 1][now_col] == -1:
                    distance[now_row + 1][now_col] = now_dist + 1
                    q.append([now_row + 1, now_col, now_dist + 1])

        # 좌
        if now_col - 1 >= 0:
            if ground[now_row][now_col - 1] == 1:
                if distance[now_row][now_col - 1] == -1:
                    distance[now_row][now_col - 1] = now_dist + 1
                    q.append([now_row, now_col - 1, now_dist + 1])

        # 우
        if now_col + 1 <= m-1:
            if ground[now_row][now_col + 1] == 1:
                if distance[now_row][now_col + 1] == -1:
                    distance[now_row][now_col + 1] = now_dist + 1
                    q.append([now_row, now_col + 1, now_dist + 1])

BFS(start_row, start_col, 0)

for line in distance:
    for num in line:
        print(num, end = " ")
    print("")