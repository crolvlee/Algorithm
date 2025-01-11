# 단방향 그래프!!!
# a가 b에 의존한다면 -> b가 감염되었을 때 a가 감염됨. a가 감염되었을 떄 b는 감염 안됨
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())    # 테스트케이스의 개수

def dijkstra(start, graph, distance, infected):
    q = []
    heapq.heappush(q, [0, start])   # [거리, 정점번호]
    distance[start] = 0
    infected[start] = True
    
    while q:
        now_dist, now_node = heapq.heappop(q)   # 시작점부터 선택점까지의 거리, 선택점
        
        if now_dist > distance[now_node]:
            continue
        
        for neighbor in graph[now_node]:
            cost = now_dist + neighbor[1]   # (시작점 ~ 선택점 거리) + (선택점 ~ 도착점 거리)
            
            if distance[neighbor[0]] > cost:
                distance[neighbor[0]] = cost
                infected[neighbor[0]] = True
                heapq.heappush(q, [cost, neighbor[0]])

for _ in range(T):
    
    # n: 컴퓨터의 개수
    # d: 의존성 개수
    # c: 해킹당한 컴퓨터의 번호
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])     # [노드번호, 거리]
        
    distance = [INF for _ in range(n+1)]    # 시작점에서 특정점까지의 거리
    infected = [False for _ in range(n+1)]  # 감염되어 있는지 여부
    
    # c에서 출발하여 한방향 탐색
    dijkstra(c, graph, distance, infected)
    
    # 출력 ================
    infected_cnt = infected.count(True)     # 총 감염되는 컴퓨터의 수
    max_distance = 0
            
    for i in range(1, n+1):
        if distance[i] > max_distance and infected[i] == True:
            max_distance = distance[i]
        
    
    print(infected_cnt, max_distance)
