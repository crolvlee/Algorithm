import sys
import heapq
input = sys.stdin.readline

tc = int(input())
#  n: 컴퓨터 개수 / d : 의존성 개수 / c: 해킹당한 컴퓨터 번호
#  a가 컴퓨터 b를 의존하며, 컴퓨터 b가 감염되면 s초 후 컴퓨터 a도 감염됨
def dijkstra(start, infection_times, graph):

    q = []
    heapq.heappush(q,(0,start))
    infection_times[start] = 0

    while q:
        time, now =heapq.heappop(q)

        if infection_times[now] < time:
            continue
  
        for a, s in graph[now]:
            now_totalTime = time + s
            if now_totalTime < infection_times[a]:
                infection_times[a] = now_totalTime
                heapq.heappush(q,(now_totalTime,a))


for t in range(tc):
    INF = int(1e9)
    n, d, c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    infection_times = [INF] * (n+1)


    for i in range(d):
        a, b, s = map(int,input().split())
        graph[b].append((a,s))
    dijkstra(c, infection_times, graph)

    cnt,last_time   = 0, 0 # 감염된 컴퓨터 수, 최종 시간
    for i in range(1, n+1):
        if infection_times[i] != INF:
            cnt +=1
            last_time = max(last_time,infection_times[i])
    print(cnt, last_time)