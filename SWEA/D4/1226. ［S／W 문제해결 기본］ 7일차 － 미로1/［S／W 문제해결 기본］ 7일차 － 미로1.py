from collections import deque

def BFS(start_row, start_col, end_row, end_col, ground):
    q = deque([])
    q.append([start_row, start_col])

    visited = [[False] * 16 for _ in range(16)]
    visited[start_row][start_col] = True

    find = 0

    while q:
        now_row, now_col = q.popleft()
        if now_row == end_row and now_col == end_col:
            find = 1
            break

        # 상
        if now_row - 1 >= 0 and ground[now_row - 1][now_col] != '1':
            if visited[now_row - 1][now_col] == False:
                q.append([now_row - 1, now_col])
                visited[now_row - 1][now_col] = True

        # 하
        if now_row + 1 <= 15 and ground[now_row + 1][now_col] != '1':
            if visited[now_row + 1][now_col] == False:
                q.append([now_row + 1, now_col])
                visited[now_row + 1][now_col] = True

        # 좌
        if now_col - 1 >= 0 and ground[now_row][now_col - 1] != '1':
            if visited[now_row][now_col - 1] == False:
                q.append([now_row, now_col - 1])
                visited[now_row][now_col - 1] = True

        # 우
        if now_col + 1 <= 15 and ground[now_row][now_col + 1] != '1':
            if visited[now_row][now_col + 1] == False:
                q.append([now_row, now_col + 1])
                visited[now_row][now_col + 1] = True

    return find

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t_c = int(input())
    ground = []

    start_row = 0
    start_col = 0
    end_row = 0
    end_col = 0

    for i in range(16):
        line = input()
        ground.append(line)

        # 시작점
        if '2' in line:
            start_row = i
            start_col = line.index('2')

        # 끝점
        if '3' in line:
            end_row = i
            end_col = line.index('3')

    # 너비 우선 BFS 실행
    answer = BFS(start_row, start_col, end_row, end_col, ground)

    print(f"#{t_c} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
