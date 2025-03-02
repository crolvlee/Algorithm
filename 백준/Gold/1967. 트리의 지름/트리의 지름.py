import sys
sys.setrecursionlimit(20000)
INF = 1e9

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    parent, child, w = map(int, input().split())

    graph[parent].append([child, w])
    graph[child].append([parent, w])


# ========================
# 리프 노드 구하기
leaf_node_list = []
for i in range(1, N + 1):
    if i not in graph:
        leaf_node_list.append(i)


# ========================
# start에서 모든 노드들까지 가는 거리 구하는 함수
def DFS(now_node, dist, distance, visited):
    distance[now_node] = dist
    visited[now_node] = True

    for neighbor in graph[now_node]:
        neighbor_node = neighbor[0]
        neighbor_dist = neighbor[1]

        if visited[neighbor_node] == False:
            DFS(neighbor_node, dist + neighbor_dist, distance, visited)


# 1. 특정 노드 A에서 가장 먼 리프 노드 B 찾기
distance_A = [0] * (N+1)
visited_A = [False] * (N+1)

DFS(1, 0, distance_A, visited_A)

max_AB = -1
node_B = -1
for idx, dist in enumerate(distance_A):
    if dist > max_AB:
        node_B = idx
        max_AB = dist

# 2. 노드 B에서 가장 먼 노드 C 찾기
distance_B = [0] * (N+1)
visited_B = [False] * (N+1)

DFS(node_B, 0, distance_B, visited_B)

max_BC = -1
node_C = -1
for idx, dist in enumerate(distance_B):
    if dist > max_BC:
        node_C = idx
        max_BC = dist

print(max_BC)
