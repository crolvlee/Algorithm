import heapq

# 입력받기
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight])


# 다익스트라 함수
def dijkstra(start):
    distance = [1e9] * (N+1)

    q = []                          # start에서 특정점까지의 거리
    heapq.heappush(q, [0, start])   # [거리, 정점번호]
    distance[start] = 0

    while q:
        now_dist, now_node = heapq.heappop(q)

        if distance[now_node] < now_dist:
            continue
        
        for neighbor in graph[now_node]:
            neighbor_node = neighbor[0]
            neighbor_cost = neighbor[1]     # now_node ~ neighbor_node까지 바로 연결된 거리

            new_dist = now_dist + neighbor_cost
            if new_dist < distance[neighbor_node]:
                distance[neighbor_node] = new_dist
                heapq.heappush(q, [new_dist, neighbor_node])

    return distance


result = [0] * (N+1)

# 1. 각각 점 -> X
for i in range(1, N+1):
    dist = dijkstra(i)
    result[i] = dist[X]

# 2. X -> 각각 점
x_dist = dijkstra(X)
for i in range(1, N+1):
    result[i] += x_dist[i]

print(max(result[1:]))