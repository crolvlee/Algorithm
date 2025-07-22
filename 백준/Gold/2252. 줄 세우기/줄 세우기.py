from collections import deque

N, M = map(int, input().split())
graph = {}
indegree = {}

for i in range(N):
    graph[i+1] = []
    indegree[i+1] = 0
    
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    indegree[v] += 1
    
# indegree가 0인 것을 큐에 넣음 (가장 앞에 올 수 있는 것들)
q = deque()
for k, v in indegree.items():
    if v == 0:
        q.append(k)
        
result = []

while q:
    now_node = q.popleft()
    result.append(now_node)
    next_node_list = graph[now_node]
    
    for next_node in next_node_list:
        indegree[next_node] -= 1
        
        if indegree[next_node] == 0:
            q.append(next_node)
        

for r in result:
    print(r, end=" ")