import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# O: 빈 공간
# X: 벽
# I: 도연
# P: 사람

# 재귀. DFS
def DFS(now_row, now_col):
    global meet_cnt
    
    visited[now_row][now_col] = True

    # 아랫쪽
    if now_row + 1 <= N-1 and visited[now_row + 1][now_col] == False:
        if ground[now_row + 1][now_col] == 'O':
            DFS(now_row + 1, now_col)
        elif ground[now_row + 1][now_col] == 'P':
            meet_cnt += 1
            DFS(now_row + 1, now_col)

    # 윗쪽
    if now_row - 1 >= 0 and visited[now_row - 1][now_col] == False:
        if ground[now_row - 1][now_col] == "O":
            DFS(now_row - 1, now_col)
        elif ground[now_row - 1][now_col] == "P":
            meet_cnt += 1
            DFS(now_row - 1, now_col)

    # 오른쪽
    if now_col + 1 <= M-1 and visited[now_row][now_col + 1] == False:
        if ground[now_row][now_col + 1] == "O":
            DFS(now_row, now_col + 1)
        elif ground[now_row][now_col + 1] == "P":
            meet_cnt += 1
            DFS(now_row, now_col + 1)

    # 왼쪽
    if now_col - 1 >= 0 and visited[now_row][now_col - 1] == False:
        if ground[now_row][now_col - 1] == "O":
            DFS(now_row, now_col - 1)
        elif ground[now_row][now_col - 1] == "P":
            meet_cnt += 1
            DFS(now_row, now_col - 1)


N, M = map(int, input().split())
ground = []
visited = [[False] * M for _ in range(N)]
I_row = -1
I_col = -1
meet_cnt = 0

for i in range(N):
    line = input()
    ground.append(line)
    
    if 'I' in line:
        I_row = i
        I_col = line.index('I')

DFS(I_row, I_col)

if meet_cnt == 0:
    print('TT')
else:
    print(meet_cnt)
