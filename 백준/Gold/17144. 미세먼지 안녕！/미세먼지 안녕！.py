import sys
input = sys.stdin.readline

# 편의상 제일 왼쪽 위를 0행 0열

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

R, C, T = map(int, input().split())
ground = []
first_air_row = -1
second_air_row = -1

for i in range(R):
    line = list(map(int, input().split()))
    ground.append(line)

    if line[0] == -1 and first_air_row == -1:
        first_air_row = i
        second_air_row = i+1

# ===========================

for _ in range(T):
    # 1. 미세먼지 확산
    change_table = [[0] * C for _ in range(R)]

    # ground 돌면서 change_table 채우기
    for now_row in range(R):
        for now_col in range(C):
            if ground[now_row][now_col] == -1:
                continue

            # 상하좌우 확인
            for d_row, d_col in directions:
                if 0 <= now_row + d_row <= R-1 and 0 <= now_col + d_col <= C-1:
                    if ground[now_row + d_row][now_col + d_col] != -1:
                        spread = ground[now_row][now_col] // 5
                        change_table[now_row][now_col] -= spread
                        change_table[now_row + d_row][now_col + d_col] += spread

    # change_table에 맞춰서 확산된 거를 ground에 반영하기
    for now_row in range(R):
        for now_col in range(C):
            ground[now_row][now_col] += change_table[now_row][now_col]

    # ======================================================
    # 2. 공기청정기 확산
    # 2-1. 위 - 반시계 방향으로 작동
    # (1) 0열 처리
    for i in range(first_air_row - 1, 0, -1):
        ground[i][0] = ground[i-1][0]

    # (2) 0행 처리
    for i in range(0, C-1):
        ground[0][i] = ground[0][i+1]

    # (3) C-1열 처리
    for i in range(0, first_air_row):
        ground[i][C-1] = ground[i+1][C-1]

    # (4) first_air_row행 처리
    for i in range(C-1, 1, -1):
        ground[first_air_row][i] = ground[first_air_row][i-1]

    ground[first_air_row][1] = 0

    # 2-2. 아래 - 시계 방향으로 작동
    # (1) 0열 처리
    for i in range(second_air_row + 1, R-1):
        ground[i][0] = ground[i+1][0]

    # (2) R-1열 처리
    for i in range(0, C-1):
        ground[R-1][i] = ground[R-1][i+1]

    # (3) C-1열 처리
    for i in range(R-1, second_air_row, -1):
        ground[i][C-1] = ground[i-1][C-1]

    # (4) second_air_row행 처리
    for i in range(C-1, 1, -1):
        ground[second_air_row][i] = ground[second_air_row][i-1]

    ground[second_air_row][1] = 0


answer = 0
for line in ground:
    for num in line:
        if num != -1:
            answer += num

print(answer)
