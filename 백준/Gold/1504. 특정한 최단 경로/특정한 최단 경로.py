import heapq
INF = 1e9

# N: 정점의 개수, E: 간선의 개수
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 꼭 거쳐야 하는 점
v1, v2 = map(int, input().split())

# =========================================

# 다익스트라 함수
def dijkstra(start, goal):
    distance = [INF] * (N + 1)      # start에서 특정점까지의 최단거리 (업데이트될 것임)
    q = []                          # start에서 특정점까지의 거리 [거리, 특정 정점번호]

    heapq.heappush(q, [0, start])   # [거리, 정점번호]
    distance[start] = 0

    while q:
        now_dist, now_node = heapq.heappop(q)   # now_dist: start ~ now_node 까지의 거리
        
        if distance[now_node] < now_dist:
            continue

        for neighbor in graph[now_node]:
            neighbor_node = neighbor[0]
            neighbor_cost = neighbor[1]             # now_node ~ neighbor_node가 바로 연결된 거리

            new_cost = now_dist + neighbor_cost     # (start ~ now_node) + (now_node ~ neighbor_node)
            if new_cost < distance[neighbor_node]:
                distance[neighbor_node] = new_cost
                heapq.heappush(q, [new_cost, neighbor_node])
                
    # start ~ goal 노드까지의 거리
    return distance[goal]


# 꼭 거쳐야하는 점
essential = dijkstra(v1, v2)

# =================================
# 케이스 1: [1 -> v1] + [v2 -> N]
result_1 = 0
first_1= dijkstra(1, v1)
last_1 = dijkstra(v2, N)

if first_1 == INF or last_1 == INF:
    result_1 = INF
else:
    result_1 = first_1 + last_1 + essential

# 케이스 2: [1 -> v2] + [v1 -> N]
result_2 = 0
first_2 = dijkstra(1, v2)
last_2 = dijkstra(v1, N)

if first_2 == INF or last_2 == INF:
    result_2 = INF
else:
    result_2 = first_2 + last_2 + essential

# =================================
# 최종 출력
if result_1 == INF and result_2 == INF:
    print(-1)
else:
    print(min(result_1, result_2))
