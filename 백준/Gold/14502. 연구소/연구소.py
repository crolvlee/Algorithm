import itertools

N, M = map(int, input().split())  # N: 세로(행 수), M: 가로(열 수)

ground = []
for _ in range(N):
    ground.append(list(map(int, input().split())))

# 바이러스 확산
def spread_virus(temp_ground):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 하, 상, 우, 좌
    queue = []

    # 바이러스 위치를 큐에 추가
    for i in range(N):
        for j in range(M):
            if temp_ground[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and temp_ground[nx][ny] == 0:
                temp_ground[nx][ny] = 2  # 바이러스 확산
                queue.append((nx, ny))

# 안전 영역 크기 계산
def calculate_safe_area(temp_ground):
    safe_area = 0
    for i in range(N):
        for j in range(M):
            if temp_ground[i][j] == 0:
                safe_area += 1
    return safe_area

max_safe_area = 0
empty_positions = [(i, j) for i in range(N) for j in range(M) if ground[i][j] == 0]

# 벽 세우기 조합 생성
for walls in itertools.combinations(empty_positions, 3):
    temp_ground = [row[:] for row in ground]  # 원본 복사
    for wx, wy in walls:
        temp_ground[wx][wy] = 1  # 벽 세우기

    spread_virus(temp_ground)  # 바이러스 퍼짐
    safe_area = calculate_safe_area(temp_ground)  # 안전 영역 계산
    max_safe_area = max(max_safe_area, safe_area)  # 최대 안전 영역 크기 갱신

print(max_safe_area)
