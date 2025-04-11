import sys
import heapq
input = sys.stdin.readline

# 편의상 제일 왼쪽 위를 0행 0열

# R: 행의 수 / C: 열의 수 / M: 상어의 수
R, C, M = map(int, input().split())
ground_dict = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    ground_dict[(r-1, c-1)] = [s, d, z]

# ===================================================
# 상하우좌
directions = {}
directions[1] = (-1, 0)
directions[2] = (1, 0)
directions[3] = (0, 1)
directions[4] = (0, -1)

# ===================================================
# 상어가 이동하는 함수
def move(now_row, now_col, now_s, now_d):
    if now_d in (1, 2):     # 상하
        cycle = 2 * (R - 1)
    else:   # 좌우
        cycle = 2 * (C - 1)

    if cycle != 0:
        now_s = now_s % cycle

    for i in range(now_s):
        # 현재 이동 방향
        d_row, d_col = directions[now_d]

        if 0 <= now_row + d_row <= R-1 and 0 <= now_col + d_col <= C-1:
            now_row += d_row
            now_col += d_col
        else:
            # 상으로 가다가 한계에 다다를 때
            if now_row + d_row < 0:
                now_d = 2
                now_row += 1
            # 하로 가다가 한계에 다다를 때
            elif now_row + d_row > R-1:
                now_d = 1
                now_row -= 1
            # 좌로 가다가 한계에 다다를 떄
            elif now_col + d_col < 0:
                now_d = 3
                now_col += 1
            # 우로 가다가 한계에 다다를 떄
            elif now_col + d_col > C-1:
                now_d = 4
                now_col -= 1

    return now_row, now_col, now_d


# ===================================================
answer = 0

for man_col in range(C):
    if len(ground_dict) == 0:
        break

    # 1. 낚시왕이 있는 열에서 행이 가장 작은 상어를 잡음
    for i in range(R):
        if (i, man_col) in ground_dict:
            s, d, z = ground_dict[(i, man_col)]
            answer += z
            ground_dict[(i, man_col)] = []
            break


    # 2. 상어가 이동
    sang_dict = {}      # 이동 후 상어의 위치를 담을 딕셔너리
    for i in range(R):
        for j in range(C):
            q = []
            heapq.heapify(q)
            sang_dict[(i, j)] = q

    # 실제 이동 (ground_dict에 있는 것을 바탕으로)
    for now_pos, now_sang in ground_dict.items():
        if len(now_sang) == 0:
            continue

        now_row = now_pos[0]
        now_col = now_pos[1]
        now_s, now_d, now_z = now_sang[0], now_sang[1], now_sang[2]

        after_row, after_col, after_d = move(now_row, now_col, now_s, now_d)
        heapq.heappush(sang_dict[(after_row, after_col)], [-now_z, now_s, after_d])

    # ground_dict를 초기화하기
    ground_dict = {}

    # sang_dict를 바탕으로 ground_dict 새로 채워넣기
    # 한 칸에 가장 사이즈가 큰 상어만 남기기!
    for sang_pos, sang_q in sang_dict.items():
        sang_row = sang_pos[0]
        sang_col = sang_pos[1]

        if len(sang_q) > 0:
            z_minus, s, d = heapq.heappop(sang_q)
            ground_dict[(sang_row, sang_col)] = [s, d, -z_minus][:]


print(answer)