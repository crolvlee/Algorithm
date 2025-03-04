import heapq
INF = 1e9

def dijkstra(start):
    q = []              # [[start ~ 특정점 k까지의 최단거리, 특정점 k], [], ...]
    heapq.heappush(q, [0, start])
    distance[start] = 0
    
    while q:
        now_dist, now_node = heapq.heappop(q)    # now_dist: start ~ now_node까지의 거리
        
        if now_dist > distance[now_node]:
            continue
        
        for neighbor in graph[now_node]:
            new_dist = now_dist + 1         # new_dist: start ~ neighbor까지의 거리
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(q, [new_dist, neighbor])

def solution(n, edge):
    global graph
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        u = e[0]
        v = e[1]
        graph[u].append(v)
        graph[v].append(u)
        
    global distance
    distance = [INF] * (n+1)  # i번째에 있는 값: i점 ~ start까지의 최단거리
    
    dijkstra(1)
    
    max_dist = max(distance[1:])
    answer = distance.count(max_dist)
    return answer