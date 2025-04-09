# 편의상 제일 왼쪽 윗 칸을 (0, 0)으로 하겠음

# N: 열의 수 / M: 이미 존재하는 가로 사다리 개수 / H: 행의 수
N, M, H = map(int, input().split())
exist = [[0] * N for _ in range(H)]

for _ in range(0, M):
    a, b = map(int, input().split())
    exist[a-1][b-1] = 1

# =====================================
# 현재 칸에서 시작하는 사다리를 놓을 수 있는지 검증하는 함수 구현
def validate(now_row, now_col):
    if now_col == 0:
        if exist[now_row][now_col] == 1:
            return False

        if exist[now_row][now_col + 1] == 1:
            return False

    else:
        if exist[now_row][now_col - 1] == 1:
            return False

        if exist[now_row][now_col] == 1:
            return False

        if exist[now_row][now_col + 1] == 1:
            return False

    return True

# =====================================
# 시작점이 도착하는 곳은 어딘지 확인
def find_end(start):
    now_row = 0
    now_col = start

    while True:
        if now_row == H:
            break

        # 1. 오른쪽으로 갈 수 있으면 -> 오른쪽으로 가기
        if exist[now_row][now_col] == 1:
            now_col += 1

        # 2. 왼쪽으로 갈 수 있다면 -> 왼쪽으로 가기
        elif now_col - 1 >= 0 and exist[now_row][now_col - 1] == 1:
            now_col -= 1

        # 3. 아래로 내려가기
        now_row += 1

    return now_col




# =====================================
# a에서 a로 갈 수 있는지 확인
def check_a_to_a():
    result = True
    for i in range(0, N):
        if find_end(i) == i:
            continue
        else:
            result = False
            break

    return result


# =====================================
answer = 1e9

# 깊이우선 DFS 함수 구현
def DFS(now_row, now_col, depth):
    global answer

    if depth == 4:
        return

    if check_a_to_a() == True:
        answer = min(depth, answer)

    for i in range(now_row, H):
        if i == now_row:
            for j in range(now_col, N-1):
                can_ga_ladder = validate(i, j)
                if can_ga_ladder == True:
                    exist[i][j] = 1
                    DFS(i, j, depth + 1)
                    exist[i][j] = 0
        else:
            for j in range(0, N-1):
                can_ga_ladder = validate(i, j)
                if can_ga_ladder == True:
                    exist[i][j] = 1
                    DFS(i, j, depth + 1)
                    exist[i][j] = 0


if check_a_to_a() == True:
    print(0)
else:
    DFS(0, 0, 0)
    if answer == 1e9:
        print(-1)
    else:
        print(answer)
