import heapq

def solution(n, roads, sources, destination):
    # 1. 그래프 만들기
    graph = {}
    for i in range(1, n+1):
        graph[i] = []
        
    for road in roads:
        u = road[0]
        v = road[1]
        graph[u].append(v)
        graph[v].append(u)
        
    # 2. 최단거리 초기화
    distances = [1e9] * (n+1)
    visited = [False] * (n+1)
    
    # 다익스트라 함수
    def dijkstra(start):
        q = []
        heapq.heappush(q, [0, start])  # [현재점~시작점까지의 거리, 현재점]
        distances[start] = 0
        visited[start] = True
        
        while q:
            now_dist, now_node = heapq.heappop(q)
            visited[now_node] = True
            
            if distances[now_node] < now_dist:
                continue
                
            for neighbor_node in graph[now_node]:
                new_dist = now_dist + 1
                if new_dist < distances[neighbor_node]:
                    distances[neighbor_node] = new_dist
                    heapq.heappush(q, [new_dist, neighbor_node])
        
    dijkstra(destination)
    
    
    answer = []
    for s in sources:
        if visited[s] == False:
            answer.append(-1)
        else:
            answer.append(distances[s])
    
    return answer