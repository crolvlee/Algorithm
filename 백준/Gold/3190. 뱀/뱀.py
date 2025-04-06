from collections import deque

# 편의상 0부터 시작

# ground
N = int(input())
ground = [[0] * N for _ in range(N)]

# 사과의 위치
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    ground[a-1][b-1] = 1

# 회전 시각, 방향 정의
L = int(input())
rotate_list = []
for _ in range(L):
    time, direction = map(str, input().split())
    time = int(time)
    rotate_list.append([time, direction])


# =========================================
# 회전 방향 관련 [key의 L, key의 D]
rotate_dict = {'LEFT': ['DOWN', 'UP'], 'RIGHT': ['UP', 'DOWN'], 'UP': ['LEFT', 'RIGHT'], 'DOWN': ['RIGHT', 'LEFT']}

# 뱀 위치 설정
ground[0][0] = 2

# 시간에 따라 뱀 이동
now_time = 0
now_direction = 'RIGHT'
now_head_row = 0
now_head_col = 0

snake_pos = deque()
snake_pos.append([now_head_row, now_head_col])

while True:
    now_time += 1

    # 상
    if now_direction == 'UP':
        # 벽인 경우
        if now_head_row - 1 == -1:
            break

        # 머리 이동할 곳이 몸인 경우
        if ground[now_head_row - 1][now_head_col] == 2:
            break

        # 머리 이동할 곳에 사과가 있는 경우
        if ground[now_head_row - 1][now_head_col] == 1:
            ground[now_head_row - 1][now_head_col] = 2
            now_head_row -= 1
            snake_pos.appendleft([now_head_row, now_head_col])

        # 머리 이동할 곳에 사과가 없는 경우
        elif ground[now_head_row - 1][now_head_col] == 0:
            ground[now_head_row - 1][now_head_col] = 2
            now_head_row -= 1
            snake_pos.appendleft([now_head_row, now_head_col])
            tail_row, tail_col = snake_pos.pop()
            ground[tail_row][tail_col] = 0

    # 하
    elif now_direction == 'DOWN':
        # 벽인 경우
        if now_head_row + 1 == N:
            break

        # 머리 이동할 곳이 몸인 경우
        if ground[now_head_row + 1][now_head_col] == 2:
            break

        # 머리 이동할 곳에 사과가 있는 경우
        if ground[now_head_row + 1][now_head_col] == 1:
            ground[now_head_row + 1][now_head_col] = 2
            now_head_row += 1
            snake_pos.appendleft([now_head_row, now_head_col])

        # 머리 이동할 곳에 사과가 없는 경우
        elif ground[now_head_row + 1][now_head_col] == 0:
            ground[now_head_row + 1][now_head_col] = 2
            now_head_row += 1
            snake_pos.appendleft([now_head_row, now_head_col])
            tail_row, tail_col = snake_pos.pop()
            ground[tail_row][tail_col] = 0

    # 좌
    elif now_direction == 'LEFT':
        # 벽인 경우
        if now_head_col - 1 == -1:
            break

        # 머리 이동할 곳이 몸인 경우
        if ground[now_head_row][now_head_col - 1] == 2:
            break

        # 머리 이동할 곳에 사과가 있는 경우
        if ground[now_head_row][now_head_col - 1] == 1:
            ground[now_head_row][now_head_col - 1] = 2
            now_head_col -= 1
            snake_pos.appendleft([now_head_row, now_head_col])

        # 머리 이동할 곳에 사과가 없는 경우
        elif ground[now_head_row][now_head_col - 1] == 0:
            ground[now_head_row][now_head_col - 1] = 2
            now_head_col -= 1
            snake_pos.appendleft([now_head_row, now_head_col])
            tail_row, tail_col = snake_pos.pop()
            ground[tail_row][tail_col] = 0


    # 우
    elif now_direction == 'RIGHT':
        # 벽인 경우
        if now_head_col + 1 == N:
            break

        # 머리 이동할 곳이 몸인 경우
        if ground[now_head_row][now_head_col + 1] == 2:
            break

        # 머리 이동할 곳에 사과가 있는 경우
        if ground[now_head_row][now_head_col + 1] == 1:
            ground[now_head_row][now_head_col + 1] = 2
            now_head_col += 1
            snake_pos.appendleft([now_head_row, now_head_col])

        # 머리 이동할 곳에 사과가 없는 경우
        elif ground[now_head_row][now_head_col + 1] == 0:
            ground[now_head_row][now_head_col + 1] = 2
            now_head_col += 1
            snake_pos.appendleft([now_head_row, now_head_col])
            tail_row, tail_col = snake_pos.pop()
            ground[tail_row][tail_col] = 0

    # 회전
    for r in rotate_list:
        if r[0] == now_time:
            # L 회전
            if r[1] == 'L':
                now_direction = rotate_dict[now_direction][0]

            # D 회전
            elif r[1] == 'D':
                now_direction = rotate_dict[now_direction][1]


print(now_time)