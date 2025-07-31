from collections import deque

N = int(input())    # 도시의 수
M = int(input())    # 여행 계획에 속한 도시의 수

# 그래프 정의
graph = {}
for k in range(1, N+1):
    graph[k] = []

for a in range(1, N+1):
    line = list(map(int, input().split()))
    for b in range(1, N+1):
        if line[b-1] == 1:
            graph[a].append(b)


# 경로 갈 수 있는지 확인하는 함수
def BFS(start, end):
    if start == end:
        return True
    
    visited = [False] * (N + 1)
    q = deque()
    for neighbor in graph[start]:
        q.append(neighbor)
        visited[neighbor] = True

    while q:
        now_point = q.popleft()
        if now_point == end:
            return True
        else:
            for neighbor in graph[now_point]:
                if visited[neighbor] == False:
                    q.append(neighbor)
                    visited[neighbor] = True

    return False


# 경로 찾기
way = list(map(int, input().split()))
answer = "YES"
for x in range(len(way) - 1):
    start = way[x]
    end = way[x+1]

    if BFS(start, end) == False:
        answer = "NO"
        break

print(answer)
