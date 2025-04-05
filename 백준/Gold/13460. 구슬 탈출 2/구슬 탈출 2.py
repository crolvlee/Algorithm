from collections import deque

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(row, col, d_row, d_col):
    move_cnt = 0
    while True:
        # 현재 위치가 구멍이라면 멈춤
        if ground[row][col] == 'O':
            break

        # 다음 위치가 벽이라면 멈춤
        if ground[row + d_row][col + d_col] == '#':
            break

        row += d_row
        col += d_col
        move_cnt += 1

    return row, col, move_cnt


def BFS(red_row, red_col, blue_row, blue_col):
    q = deque()
    q.append([red_row, red_col, blue_row, blue_col, 0])
    visited = set()
    visited.add((red_row, red_col, blue_row, blue_col))

    while q:
        now_red_row, now_red_col, now_blue_row, now_blue_col, now_depth = q.popleft()
        if now_depth == 10:
            return -1

        for d_row, d_col in directions:
            # 빨간 구슬 이동
            next_red_row, next_red_col, red_moves = move(now_red_row, now_red_col, d_row, d_col)

            # 파란 구슬 이동
            next_blue_row, next_blue_col, blue_moves = move(now_blue_row, now_blue_col, d_row, d_col)

            # ===================
            # 파란 구슬이 구멍에 들어가면 실패
            if ground[next_blue_row][next_blue_col] == 'O':
                continue

            # 빨간 구슬이 구멍에 들어가면 성공
            if ground[next_red_row][next_red_col] == 'O':
                return now_depth + 1

            # 두 구슬이 같은 위치에 있으면, 더 많이 이동한 구슬은 한 칸 뒤로 옮김
            if next_red_row == next_blue_row and next_red_col == next_blue_col:
                if red_moves > blue_moves:
                    next_red_row -= d_row
                    next_red_col -= d_col
                else:
                    next_blue_row -= d_row
                    next_blue_col -= d_col

            # 방문하지 않은 위치라면 큐에 추가
            if (next_red_row, next_red_col, next_blue_row, next_blue_col) not in visited:
                visited.add((next_red_row, next_red_col, next_blue_row, next_blue_col))
                q.append([next_red_row, next_red_col, next_blue_row, next_blue_col, now_depth + 1])

    return -1

N, M = map(int, input().split())
ground = []

red_row = 0
red_col = 0
blue_row = 0
blue_col = 0

for i in range(N):
    line = input()
    ground.append(line)

    # R 확인
    if 'R' in line:
        red_row = i
        red_col = line.index('R')

    # B 확인
    if 'B' in line:
        blue_row = i
        blue_col = line.index('B')


answer = BFS(red_row, red_col, blue_row, blue_col)
print(answer)