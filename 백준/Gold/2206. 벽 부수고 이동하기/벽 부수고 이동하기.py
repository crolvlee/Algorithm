from collections import deque

# 0: 이동 가능
# 1: 이동 불가능
# 벽을 1개까지 부셔도 됨

# 입력받기
N, M = map(int, input().split())
table = []
for _ in range(N):
    line = input()
    table.append(line)


# BFS 함수 정의
def BFS(table, start_row, start_col, visited):
    q = deque([])
    q.append([start_row, start_col, 1, True])     # [행번호, 열번호, 거리누적, 부시기 가능 여부]
    visited[start_row][start_col][0] = 1

    while q:
        now_row, now_col, dist, can_break = q.popleft()

        if now_row == N-1 and now_col == M-1:
            return dist

        # 상
        if now_row - 1 >= 0:
            if table[now_row - 1][now_col] == '0':
                if can_break == True:
                    if visited[now_row - 1][now_col][0] > dist + 1:
                        q.append([now_row - 1, now_col, dist + 1, can_break])
                        visited[now_row - 1][now_col][0] = dist + 1
                elif can_break == False:
                    if visited[now_row - 1][now_col][1] > dist + 1:
                        q.append([now_row - 1, now_col, dist + 1, can_break])
                        visited[now_row - 1][now_col][1] = dist + 1


            elif table[now_row - 1][now_col] == '1':
                if can_break == True:
                    if visited[now_row - 1][now_col][1] > dist + 1:
                        q.append([now_row - 1, now_col, dist + 1, False])
                        visited[now_row - 1][now_col][1] = dist + 1

        # 하
        if now_row + 1 <= N-1:
            if table[now_row + 1][now_col] == '0':
                if can_break == True:
                    if visited[now_row + 1][now_col][0] > dist + 1:
                        q.append([now_row + 1, now_col, dist + 1, can_break])
                        visited[now_row + 1][now_col][0] = dist + 1
                elif can_break == False:
                    if visited[now_row + 1][now_col][1] > dist + 1:
                        q.append([now_row + 1, now_col, dist + 1, can_break])
                        visited[now_row + 1][now_col][1] = dist + 1

            elif table[now_row + 1][now_col] == '1':
                if can_break == True:
                    if visited[now_row + 1][now_col][1] > dist + 1:
                        q.append([now_row + 1, now_col, dist + 1, False])
                        visited[now_row + 1][now_col][1] = dist + 1

        # 좌
        if now_col - 1 >= 0:
            if table[now_row][now_col - 1] == '0':
                if can_break == True:
                    if visited[now_row][now_col - 1][0] > dist + 1:
                        q.append([now_row, now_col - 1, dist + 1, can_break])
                        visited[now_row ][now_col - 1][0] = dist + 1
                elif can_break == False:
                    if visited[now_row][now_col - 1][1] > dist + 1:
                        q.append([now_row, now_col - 1, dist + 1, can_break])
                        visited[now_row][now_col - 1][1] = dist + 1

            elif table[now_row][now_col - 1] == '1':
                if can_break == True:
                    if visited[now_row][now_col - 1][1] > dist + 1:
                        q.append([now_row, now_col - 1, dist + 1, False])
                        visited[now_row][now_col - 1][1] = dist + 1

        # 우
        if now_col + 1 <= M-1:
            if table[now_row][now_col + 1] == '0':
                if can_break == True:
                    if visited[now_row][now_col + 1][0] > dist + 1:
                        q.append([now_row, now_col + 1, dist + 1, can_break])
                        visited[now_row][now_col + 1][0] = dist + 1
                elif can_break == False:
                    if visited[now_row][now_col + 1][1] > dist + 1:
                        q.append([now_row, now_col + 1, dist + 1, can_break])
                        visited[now_row][now_col + 1][1] = dist + 1

            elif table[now_row][now_col + 1] == '1':
                if can_break == True:
                    if visited[now_row][now_col + 1][1] > dist + 1:
                        q.append([now_row, now_col + 1, dist + 1, False])
                        visited[now_row][now_col + 1][1] = dist + 1

    return -1


visited = [[[1e9, 1e9] for _ in range(M)] for _ in range(N)]
result = BFS(table, 0, 0, visited)
print(result)
