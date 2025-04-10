from collections import deque

# N x N의 땅이 있음
# 맞닿아 있는 두 나라의 인구 차이가 L명 이상, R명 이하라면 -> 국경선을 엶
N, L, R = map(int, input().split())
A = []

for _ in range(N):
    line = list(map(int, input().split()))
    A.append(line)

# =========================================
# 한 그룹에 속하는 것들의 평균을 리턴
def BFS(start_row, start_col):
    q = deque()
    q.append([start_row, start_col])
    group = []
    visited[start_row][start_col] = True

    now_sum = 0
    country_cnt = 0

    while q:
        now_row, now_col = q.popleft()
        now_sum += A[now_row][now_col]
        country_cnt += 1
        group.append((now_row, now_col))

        # 상
        if now_row - 1 >= 0 and visited[now_row - 1][now_col] == False:
            diff = abs(A[now_row - 1][now_col] - A[now_row][now_col])
            if diff >= L and diff <= R:
                q.append([now_row - 1, now_col])
                visited[now_row - 1][now_col] = True

        # 하
        if now_row + 1 <= N-1 and visited[now_row + 1][now_col] == False:
            diff = abs(A[now_row + 1][now_col] - A[now_row][now_col])
            if diff >= L and diff <= R:
                q.append([now_row + 1, now_col])
                visited[now_row + 1][now_col] = True

        # 좌
        if now_col - 1 >= 0 and visited[now_row][now_col - 1] == False:
            diff = abs(A[now_row][now_col - 1] - A[now_row][now_col])
            if diff >= L and diff <= R:
                q.append([now_row, now_col - 1])
                visited[now_row][now_col - 1] = True

        # 우
        if now_col + 1 <= N-1 and visited[now_row][now_col + 1] == False:
            diff = abs(A[now_row][now_col + 1] - A[now_row][now_col])
            if diff >= L and diff <= R:
                q.append([now_row, now_col + 1])
                visited[now_row][now_col + 1] = True

    average = now_sum // country_cnt
    return average, group

# =========================================
move_cnt = 0

# 순회 1번 당 1번의 Move
while True:
    if move_cnt == 2001:
        break

    visited = [[False] * N for _ in range(N)]
    group_cnt = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                group_avg, group_list = BFS(i, j)
                group_cnt += 1

                # 같은 그룹에 있는 것들 인구 값 바꾸기
                for g_row, g_col in group_list:
                    A[g_row][g_col] = group_avg

    if group_cnt == N*N:
        break

    move_cnt += 1

print(move_cnt)