from collections import deque

N, M = map(int, input().split())
ground = []
for _ in range(N):
    line = list(map(int, input()))
    ground.append(line)
    
def BFS(ground):
    q = deque()
    q.append([0, 0, 1])    # [row, col, dist]
    ground[0][0] = -1

    while True:
        now_row, now_col, now_dist = q.popleft()

        if now_row == N-1 and now_col == M-1:
            return now_dist

        # 상
        if now_row - 1 >=0 and ground[now_row - 1][now_col] == 1:
            q.append([now_row - 1, now_col, now_dist + 1])
            ground[now_row - 1][now_col] = -1

        # 하
        if now_row + 1 <= N-1 and ground[now_row + 1][now_col] == 1:
            q.append([now_row + 1, now_col, now_dist + 1])
            ground[now_row + 1][now_col] = -1

        # 좌
        if now_col - 1 >= 0 and ground[now_row][now_col - 1] == 1:
            q.append([now_row, now_col - 1, now_dist + 1])
            ground[now_row][now_col - 1] = -1

        # 우
        if now_col + 1 <= M-1 and ground[now_row][now_col + 1] == 1:
            q.append([now_row, now_col + 1, now_dist + 1])
            ground[now_row][now_col + 1] = -1

answer = BFS(ground)
print(answer)