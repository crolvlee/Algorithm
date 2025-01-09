# N: 마을(노드)의 개수
# K: K시간 이하로만 배달 가능

import heapq

def dijkstra(start, distance, graph):
    q = []
    
    heapq.heappush(q, [0, start])  # [거리, 노드번호]를 넣음
    distance[start] = 0
    
    while q:
        # 거리가 짧은것 꺼내기
        dist, now = heapq.heappop(q)
        
        # 이미 처리된 적 있는 노드라면 무시. pop만 하고 아래 for문은 돌지 X
        if distance[now] < dist:
            continue
        
        for neighbor in graph[now]:
            cost = dist + neighbor[1]   # (start ~ 꺼낸점) + (꺼낸점 ~ 도착점)
            if cost < distance[neighbor[0]]:
                distance[neighbor[0]] = cost
                heapq.heappush(q, [cost, neighbor[0]])

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [int(1e9)] * (N+1)
    
    # 그래프에 원소 넣어주기
    for r in road:
        start, end, cost = r[0], r[1], r[2]
        graph[start].append([end, cost])
        graph[end].append([start, cost])
    
    # 다익스트라 실행
    dijkstra(1, distance, graph)

    print(distance)
    # K 이하인 원소의 수 구하기
    answer = 0
    for d in distance[1:]:
        if d <= K:
            answer += 1

    return answer