import sys
input = sys.stdin.readline

# N: 집의 개수   M: 길의 개수
N, M = map(int, input().split())

# 그래프 설정
graph = []
for _ in range(M):
    u, v, w = map(int, input().split())
    graph.append([u, v, w])

graph.sort(key = lambda x: x[2])

# 부모 노드 설정
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

# =======================================-----

# 루트부모 찾는 함수
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 서로 다른 노드 a, b의 루트부모를 같게 함
def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# =======================================-----

# 모든 점을 연결하는 간선 조합 중, 거리가 가장 작은 것 찾기
result_cost = 0
max_cost = 0

for node in graph:
    u, v, w = node
    if find_parent(u) != find_parent(v):
        union(u, v)
        result_cost += w
        max_cost = max(w, max_cost)

print(result_cost - max_cost)
