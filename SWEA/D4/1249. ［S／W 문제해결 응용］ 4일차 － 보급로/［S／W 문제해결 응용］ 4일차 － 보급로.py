from collections import deque

# 너비우선탐색
# costs에 들어간게 -1이면 아직 방문한 적 없다는 뜻
def BFS(ground, N, costs):
    q = deque([])
    costs[0][0] = 0
    q.append([0, 0])

    while q:
        now_row, now_col = q.popleft()
        now_cost = costs[now_row][now_col]

        # 상
        if now_row - 1 >= 0:
            next_cost = now_cost + int(ground[now_row - 1][now_col])
            if costs[now_row - 1][now_col] > next_cost:
                costs[now_row - 1][now_col] = next_cost
                q.append([now_row - 1, now_col])
        # 하
        if now_row + 1 <= N-1:
            next_cost = now_cost + int(ground[now_row + 1][now_col])
            if costs[now_row + 1][now_col] > next_cost:
                costs[now_row + 1][now_col] = next_cost
                q.append([now_row + 1, now_col])

        # 좌
        if now_col - 1 >= 0:
            next_cost = now_cost + int(ground[now_row][now_col - 1])
            if costs[now_row][now_col - 1] > next_cost:
                costs[now_row][now_col - 1] = next_cost
                q.append([now_row, now_col - 1])

        # 우
        if now_col + 1 <= N-1:
            next_cost = now_cost + int(ground[now_row][now_col + 1])
            if costs[now_row][now_col + 1] > next_cost:
                costs[now_row][now_col + 1] = next_cost
                q.append([now_row, now_col + 1])

    result = costs[N-1][N-1]
    return result

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    ground = []
    for _ in range(N):
        line = input()
        ground.append(line)

    costs = [[1e9] * N for _ in range(N)]

    answer = BFS(ground, N, costs)

    print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
