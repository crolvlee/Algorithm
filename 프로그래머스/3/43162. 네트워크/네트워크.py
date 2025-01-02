def DFS(point, computers, visited):
    neighbor = computers[point]
    
    for j in range(len(computers)):
        if point == j:
            continue
        
        if neighbor[j] == 1 and visited[j] == False:
            visited[j] = True
            DFS(j, computers, visited)
        

def solution(n, computers):
    visited = [False] * n
    group = 0
    
    for i in range(n):
        if visited[i] == False:
            group += 1
            DFS(i, computers, visited)
    
    
    answer = group
    return answer