from collections import deque

# 0: 빈 칸
# 1: 벽
# 2: 바이러스

# N: 세로, M: 가로
N, M = map(int, input().split())
ground = []
for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)

# 0의 위치 배열
pos_list = []
for i in range(N):
    for j in range(M):
        if ground[i][j] == 0:
            pos_list.append([i, j])

# ==================================================

# 조합 찾는 함수
def combi(num, k):
    result = []
    path = []

    def DFS(start, depth):
        if depth == k:
            result.append(path[:])
            return

        for i in range(start, num):
            path.append(i)
            DFS(i + 1, depth + 1)
            path.pop()

    DFS(0, 0)
    return result


# 바이러스 퍼뜨리는 함수
def spread(new_ground):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    q = deque()

    # 제일 처음 큐
    for i in range(N):
        for j in range(M):
            if new_ground[i][j] == 2:
                q.append([i, j])

    # 큐에 담긴 것에 따라 확산시키기
    while q:
        now_row, now_col = q.popleft()

        for d_row, d_col in directions:
            if 0 <= now_row + d_row <= N-1 and 0 <= now_col + d_col <= M-1:
                if new_ground[now_row + d_row][now_col + d_col] == 0:
                    new_ground[now_row + d_row][now_col + d_col] = 2
                    q.append([now_row + d_row, now_col + d_col])
    
    return new_ground


# 안전 영역 찾는 함수
def find_safe(ground):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 0:
                cnt += 1
    
    return cnt


# ==================================================
# 조합 배열
combi_list = combi(len(pos_list), 3)

# 안전 영역 조합
result_list = []

for com in combi_list:
    new_ground = [line[:] for line in ground]
    for a in com:
        r, c = pos_list[a]
        new_ground[r][c] = 1

    # 확산시키고, 안전 영역 찾기
    spread_ground = spread(new_ground)
    result = find_safe(spread_ground)
    result_list.append(result)


print(max(result_list))
