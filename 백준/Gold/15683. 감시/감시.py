# N: 세로 크기 / M: 가로 크기
N, M = map(int, input().split())

ground = []
for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)

# ============================================
# (상, 하, 좌, 우)
directions = {}
directions[1] = [(0, 0, 0, 1), (0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0)]
directions[2] = [(0, 0, 1, 1), (1, 1, 0, 0)]
directions[3] = [(1, 0, 0, 1), (1, 0, 1, 0), (0, 1, 0, 1), (0, 1, 1, 0)]
directions[4] = [(1, 0, 1, 1), (1, 1, 0, 1), (1, 1, 1, 0), (0, 1, 1, 1)]
directions[5] = [(1, 1, 1, 1)]


# ============================================
# CCTV 있는 좌표별 가능한 CCTV 종류를 담아둠
point_cctv_dict = {}
point_cctv = []     # BFS에서 depth 확인용

for r_idx, line in enumerate(ground):
    for c_idx, square in enumerate(line):
        cctv_num = ground[r_idx][c_idx]
        if cctv_num in [1, 2, 3, 4, 5]:
            point_cctv_dict[(r_idx, c_idx)] = directions[cctv_num][:]
            point_cctv.append((r_idx, c_idx))

A = len(point_cctv)

# ============================================
# ground의 사각지대 수 구하기
def count_spot(selected_dict):
    # 볼 수 있는 곳은 #로 표시하기
    new_ground = []
    for line in ground:
        new_line = []
        for num in line:
            new_line.append(num)
        new_ground.append(new_line)

    for cctv_pos, direction in selected_dict.items():
        cctv_row = cctv_pos[0]
        cctv_col = cctv_pos[1]

        # 상
        if direction[0] == 1:
            now_row = cctv_row
            now_col = cctv_col
            while True:
                if now_row - 1 >= 0 and new_ground[now_row - 1][now_col] != 6:
                    if new_ground[now_row - 1][now_col] == 0:
                        new_ground[now_row - 1][now_col] = '#'
                    now_row -= 1
                else:
                    break

        # 하
        if direction[1] == 1:
            now_row = cctv_row
            now_col = cctv_col
            while True:
                if now_row + 1 <= N-1 and new_ground[now_row + 1][now_col] != 6:
                    if new_ground[now_row + 1][now_col] == 0:
                        new_ground[now_row + 1][now_col] = '#'
                    now_row += 1
                else:
                    break

        # 좌
        if direction[2] == 1:
            now_row = cctv_row
            now_col = cctv_col
            while True:
                if now_col - 1 >= 0 and new_ground[now_row][now_col - 1] != 6:
                    if new_ground[now_row][now_col - 1] == 0:
                        new_ground[now_row][now_col - 1] = '#'
                    now_col -= 1
                else:
                    break

        # 우
        if direction[3] == 1:
            now_row = cctv_row
            now_col = cctv_col
            while True:
                if now_col + 1 <= M-1 and new_ground[now_row][now_col + 1] != 6:
                    if new_ground[now_row][now_col + 1] == 0:
                        new_ground[now_row][now_col + 1] = '#'
                    now_col += 1
                else:
                    break

    # new_ground로 사각지대 수 세기
    result = 0
    for line in new_ground:
        for num in line:
            if num == 0:
                result += 1

    return result


# ============================================
final_list = []

# 깊이우선 BFS 정의
def BFS(selected_dict, depth):
    if depth == A:
        # 선택된 방향일 때의 ground 사각지대 수 구하기
        result = count_spot(selected_dict)
        final_list.append(result)
        return

    now_cctv_pos = point_cctv[depth]
    for direction in point_cctv_dict[now_cctv_pos]:
        selected_dict[now_cctv_pos] = direction
        BFS(selected_dict, depth + 1)
        del selected_dict[now_cctv_pos]


BFS({}, 0)

print(min(final_list))

