from collections import deque

# 편의상 제일 왼쪽 위가 (0, 0)

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# N x N 크기의 ground
# M: 처음 활성화 바이러스의 수
N, M = map(int, input().split())
ground = []
virus_pos_list = []

# 빈칸 개수
empty_cnt = 0

for i in range(N):
    line = []
    input_line = list(map(int, input().split()))

    for j, num in enumerate(input_line):
        if num == 0:
            line.append(-1)
            empty_cnt += 1
        elif num == 1:
            line.append('X')
        elif num == 2:
            line.append('*')
            virus_pos_list.append((i, j))

    ground.append(line)




# =======================================
# 특정 조합일 때, 모든 빈 칸에 바이러스를 퍼뜨리는데 걸리는 최소 시간을 구하는 함수
# 모든 빈칸에 퍼뜨릴 수 없는 경우 -> -1 리턴
def BFS(selection):
    global empty_cnt
    spread_cnt = 0

    new_ground = []
    for line in ground:
        new_line = []
        for num in line:
            new_line.append(num)
        new_ground.append(new_line)

    q = deque()

    for virus_pos in selection:
        virus_row = virus_pos[0]
        virus_col = virus_pos[1]
        new_ground[virus_row][virus_col] = '@'
        q.append((virus_row, virus_col, 0))

    while q:
        now_row, now_col, now_time = q.popleft()

        # 상하좌우 퍼뜨리기
        for d_row, d_col in directions:
            next_row = now_row + d_row
            next_col = now_col + d_col
            if 0 <= next_row <= N-1 and 0 <= next_col <= N-1:
                # 이 2가지 경우일 때만 바꾸고, q에 추가할 수 있음
                # 이동할 곳이 빈 칸인 경우
                if new_ground[next_row][next_col] == -1:
                    new_ground[next_row][next_col] = now_time + 1
                    q.append((next_row, next_col, now_time + 1))
                    spread_cnt += 1

                    if spread_cnt == empty_cnt:
                        return now_time + 1


                # 이동할 곳에 비활성화 바이러스가 있는 경우
                if new_ground[next_row][next_col] == '*':
                    new_ground[next_row][next_col] = now_time + 1
                    q.append((next_row, next_col, now_time + 1))


    return -1


# =======================================
# 조합을 찾는 함수 DFS
def DFS(depth, start_idx, selection):
    if depth == M:
        result = BFS(selection)

        if result != -1:
            answer_list.append(result)

    for now_idx in range(start_idx, len(virus_pos_list)):
        now_virus_pos = virus_pos_list[now_idx]

        if now_virus_pos not in selection:
            DFS(depth + 1, now_idx + 1, selection + [now_virus_pos])



# =======================================

already_full = True

for line in ground:
    for num in line:
        if num == -1:   # 빈칸
            already_full = False
            break

if already_full == True:
    print(0)
else:
    answer_list = []
    DFS(0, 0, [])

    if len(answer_list) == 0:
        print(-1)
    else:
        print(min(answer_list))

