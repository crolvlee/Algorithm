import sys
input = sys.stdin.readline

# 편의상
# 시작끝점을 0행 1열 (0, 1)
# 도착끝점을 N-1행 N-1열 (N-1, N-1)

# DFS함수 정의
def DFS(ground, N, now_row, now_col, now_pipe):
    global answer
    if now_row == N-1 and now_col == N-1:
        answer += 1
        return

    # 1. 현재 파이프가 가로인 경우
    if now_pipe == "ga":
        # 가로 방향 이동
        if now_col + 1 <= N - 1:
            if ground[now_row][now_col + 1] == 0:
                DFS(ground, N, now_row, now_col + 1, "ga")

        # 대각선 방향 이동
        if now_col + 1 <= N - 1 and now_row + 1 <= N - 1:
            if ground[now_row][now_col + 1] == 0 and ground[now_row + 1][now_col + 1] == 0 and ground[now_row + 1][now_col] == 0:
                DFS(ground, N, now_row + 1, now_col + 1, "dae")

    # 2. 현재 파이프가 세로인 경우
    elif now_pipe == "se":
        # 세로 방향 이동
        if now_row + 1 <= N - 1:
            if ground[now_row + 1][now_col] == 0:
                DFS(ground, N, now_row + 1, now_col, "se")

        # 대각선 방향 이동
        if now_col + 1 <= N - 1 and now_row + 1 <= N - 1:
            if ground[now_row][now_col + 1] == 0 and ground[now_row + 1][now_col + 1] == 0 and ground[now_row + 1][now_col] == 0:
                DFS(ground, N, now_row + 1, now_col + 1, "dae")

    # 3. 현재 파이프가 대각선인 경우
    elif now_pipe == "dae":
        # 가로 방향 이동
        if now_col + 1 <= N - 1:
            if ground[now_row][now_col + 1] == 0:
                DFS(ground, N, now_row, now_col + 1, "ga")
                
        # 세로 방향 이동
        if now_row + 1 <= N - 1:
            if ground[now_row + 1][now_col] == 0:
                DFS(ground, N, now_row + 1, now_col, "se")

        # 대각선 방향 이동
        if now_col + 1 <= N - 1 and now_row + 1 <= N - 1:
            if ground[now_row][now_col + 1] == 0 and ground[now_row + 1][now_col + 1] == 0 and ground[now_row + 1][now_col] == 0:
                DFS(ground, N, now_row + 1, now_col + 1, "dae")


# 입력받기
N = int(input())
ground = []
for i in range(N):
    line = list(map(int, input().split()))
    ground.append(line)

# DFS함수 실행
answer = 0
DFS(ground, N, 0, 1, "ga")

print(answer)
