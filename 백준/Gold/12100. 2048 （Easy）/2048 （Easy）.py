from collections import deque

# 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 일단 미는 함수 정의
def push(ground, d_row, d_col, N):
    new_ground = [[0] * N for _ in range(N)]

    # 상
    if d_row == - 1 and d_col == 0:
        for col in range(0, N):
            row_pos = 0     # row_pos행 col열에 채워 넣어야 함
            for row in range(0, N):
                if ground[row][col] != 0:
                    new_ground[row_pos][col] = ground[row][col]
                    row_pos += 1

    # 하
    elif d_row == 1 and d_col == 0:
        for col in range(0, N):
            row_pos = N-1   # row_pos행 col열에 채워 넣어야 함
            for row in range(N-1, -1, -1):
                if ground[row][col] != 0:
                    new_ground[row_pos][col] = ground[row][col]
                    row_pos -= 1

    # 좌
    elif d_row == 0 and d_col == -1:
        for row in range(0, N):
            col_pos = 0
            for col in range(0, N):
                if ground[row][col] != 0:
                    new_ground[row][col_pos] = ground[row][col]
                    col_pos += 1

    # 우
    else:
        for row in range(0, N):
            col_pos = N-1
            for col in range(N-1, -1, -1):
                if ground[row][col] != 0:
                    new_ground[row][col_pos] = ground[row][col]
                    col_pos -= 1

    return new_ground

# 같은 것 만나면 합치는 함수 정의
def merge(ground, d_row, d_col, N):

    # 상
    if d_row == -1 and d_col == 0:
        for col in range(0, N):
            for row in range(0, N):
                if row + 1 <= N-1 and ground[row][col] == ground[row+1][col]:
                    ground[row][col] = ground[row][col] * 2
                    ground[row+1][col] = 0

    # 하
    elif d_row == 1 and d_col == 0:
        for col in range(0, N):
            for row in range(N-1, -1, -1):
                if row - 1 >= 0 and ground[row][col] == ground[row-1][col]:
                    ground[row][col] = ground[row][col] * 2
                    ground[row-1][col] = 0

    # 좌
    elif d_row == 0 and d_col == -1:
        for row in range(0, N):
            for col in range(0, N):
                if col + 1 <= N-1 and ground[row][col] == ground[row][col+1]:
                    ground[row][col] = ground[row][col] * 2
                    ground[row][col+1] = 0

    # 우
    else:
        for row in range(0, N):
            for col in range(N-1, -1, -1):
                if col - 1 >= 0 and ground[row][col] == ground[row][col-1]:
                    ground[row][col] = ground[row][col] * 2
                    ground[row][col-1] = 0

    return ground

# 너비우선 BFS 정의
def BFS(ground, N):
    visited = []
    visited.append(ground)
    q = deque()
    q.append([ground, 0])

    max_num = - 1

    while q:
        now_ground, now_depth = q.popleft()

        # 현재 상태에서 가장 큰 값 확인
        for line in now_ground:
            line_max = max(line)
            max_num = max(max_num, line_max)

        # 깊이가 5인 것 나타나면
        if now_depth == 5:
            continue


        for d_row, d_col in directions:
            # 1. 밀기
            ground_1 = push(now_ground, d_row, d_col, N)
            # 2. 합치기
            ground_2 = merge(ground_1, d_row, d_col, N)
            # 3. 밀기
            ground_3 = push(ground_2, d_row, d_col, N)

            # 최종 만들어진 ground가 visited에 없다면, 추가
            if ground_3 not in visited:
                q.append([ground_3, now_depth + 1])
                if ground_3 not in visited:
                    visited.append(ground_3)



    return max_num


N = int(input())
ground = []

for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)

answer = BFS(ground, N)
print(answer)