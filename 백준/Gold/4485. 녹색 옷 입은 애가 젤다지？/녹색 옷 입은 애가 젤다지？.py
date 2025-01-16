import sys
import heapq

input = sys.stdin.readline
INF = 1e9


# 다익스트라 함수
def dijkstra(ground, distance, start_row, start_col, N):
    q = []
    heapq.heappush(q, [ground[start_row][start_col], start_row, start_col])  # [거리, 정점 행, 정점 열]
    distance[start_row][start_col] = ground[start_row][start_col]

    while q:
        now_dist, now_row, now_col = heapq.heappop(q)  # 시작점부터 선택점까지의 거리, 선택점의 행, 선택점의 열

        if now_dist > distance[now_row][now_col]:
            continue

        neighbor_list = []  # 이웃점의 행, 이웃점의 열, 현재점~이웃점 사이의 거리
        # 상
        if now_row >= 1:
            neighbor_list.append([now_row - 1, now_col, ground[now_row - 1][now_col]])
        # 하
        if now_row <= N - 2:
            neighbor_list.append([now_row + 1, now_col, ground[now_row + 1][now_col]])
        # 좌
        if now_col >= 1:
            neighbor_list.append([now_row, now_col - 1, ground[now_row][now_col - 1]])
        # 우
        if now_col <= N - 2:
            neighbor_list.append([now_row, now_col + 1, ground[now_row][now_col + 1]])

        for neighbor in neighbor_list:
            cost = now_dist + neighbor[2]  # (시작점~선택점까지의 거리) + (선택점~이웃점까지의 거리)
            if cost < distance[neighbor[0]][neighbor[1]]:
                distance[neighbor[0]][neighbor[1]] = cost
                heapq.heappush(q, [cost, neighbor[0], neighbor[1]])


end = False
test = 1
while end == False:
    N = int(input())
    if N == 0:
        break

    distance = [[INF] * N for _ in range(N)]
    ground = []
    for _ in range(N):
        line = list(map(int, input().split()))
        ground.append(line)

    dijkstra(ground, distance, 0, 0, N)

    print("Problem {}: {}".format(test, distance[N - 1][N - 1]))
    test += 1
