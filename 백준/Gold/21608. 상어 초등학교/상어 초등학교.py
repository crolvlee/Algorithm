# 편의상 시작을 (0, 0)으로 하겠음

N = int(input())
student_dict = {}

for _ in range(0, N*N):
    line = list(map(int, input().split()))
    student_dict[line[0]] = line[1:]

ground = [[0] * N for _ in range(N)]

# ==================================================
def count_neighbor_like(now_row, now_col, student_num):
    cnt = 0
    student_num_like = student_dict[student_num]

    # 동
    if now_col + 1 <= N - 1:
        if ground[now_row][now_col + 1] in student_num_like:
            cnt += 1

    # 서
    if now_col - 1 >= 0:
        if ground[now_row][now_col - 1] in student_num_like:
            cnt += 1

    # 남
    if now_row + 1 <= N-1:
        if ground[now_row + 1][now_col] in student_num_like:
            cnt += 1

    # 북
    if now_row - 1 >= 0:
        if ground[now_row - 1][now_col] in student_num_like:
            cnt += 1

    return cnt


def count_neighbor_empty(now_row, now_col):
    cnt = 0

    # 동
    if now_col + 1 <= N-1:
        if ground[now_row][now_col + 1] == 0:
            cnt += 1

    # 서
    if now_col - 1 >= 0:
        if ground[now_row][now_col - 1] == 0:
            cnt += 1

    # 남
    if now_row + 1 <= N-1:
        if ground[now_row + 1][now_col] == 0:
            cnt += 1

    # 북
    if now_row - 1 >= 0:
        if ground[now_row - 1][now_col] == 0:
            cnt += 1

    return cnt

# ==================================================

for student, like_list in student_dict.items():

    # 1. 전체 칸 돌면서 칸마다 인접 좋아하는 학생 수 구하기
    like_cnt_table = [[-1] * N for _ in range(N)]

    for r_idx, line in enumerate(ground):
        for c_idx, square in enumerate(line):
            if ground[r_idx][c_idx] != 0:
                continue
            like_cnt = count_neighbor_like(r_idx, c_idx, student)
            like_cnt_table[r_idx][c_idx] = like_cnt


    # like_cnt_table에서 가장 큰 수 찾기
    max_like_cnt = 0
    for line in like_cnt_table:
        if max(line) > max_like_cnt:
            max_like_cnt = max(line)

    # ================================================================
    # 2. 가장 큰 수 적혀 있는 칸 돌기
    # 그 중 인접 빈 칸 수 세기
    neighbor_empty_cnt_table = [[-1] * N for _ in range(N)]

    for r_idx, line in enumerate(like_cnt_table):
        for c_idx, square in enumerate(line):
            if ground[r_idx][c_idx] != 0:
                continue

            if like_cnt_table[r_idx][c_idx] == max_like_cnt:
                neighbor_empty_cnt = count_neighbor_empty(r_idx, c_idx)
                neighbor_empty_cnt_table[r_idx][c_idx] = neighbor_empty_cnt

    # neighbor_empty_cnt_table에서 가장 큰 수 찾기
    max_neighbor_empty_cnt = 0
    for line in neighbor_empty_cnt_table:
        if max(line) > max_neighbor_empty_cnt:
            max_neighbor_empty_cnt = max(line)

    # ================================================================
    # 3. min_neighbor_empty_cnt인 칸 나오면 ground 그 칸에 현재 stuent num 넣기
    for r_idx, line in enumerate(neighbor_empty_cnt_table):
        finish = False
        for c_idx, square in enumerate(line):
            if neighbor_empty_cnt_table[r_idx][c_idx] == max_neighbor_empty_cnt:
                if ground[r_idx][c_idx] == 0:
                    ground[r_idx][c_idx] = student
                    finish = True
                    break

        if finish == True:
            break




# ================================================================
# ================================================================
answer = 0
for r_idx, line in enumerate(ground):
    for c_idx, square in enumerate(line):
        like_cnt = count_neighbor_like(r_idx, c_idx, square)

        if like_cnt == 0:
            answer += 0
        elif like_cnt == 1:
            answer += 1
        elif like_cnt == 2:
            answer += 10
        elif like_cnt == 3:
            answer += 100
        else:
            answer += 1000


print(answer)