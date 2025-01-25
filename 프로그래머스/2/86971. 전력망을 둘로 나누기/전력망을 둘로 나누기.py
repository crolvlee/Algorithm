# DFS -> 재귀

def DFS(graph, current, u, v, visited):
    visited[current] = True
    
    for neighbor in graph[current]:
        if u == current and v == neighbor:
            continue
        
        if visited[neighbor] == False:
            DFS(graph, neighbor, u, v, visited)


def solution(n, wires):
    diff_list = []
    
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        u = wire[0]
        v = wire[1]
        graph[u].append(v)
        graph[v].append(u)
    
    # 제거할 wire 찾기
    for wire in wires:
        u = wire[0]
        v = wire[1]
        visited = [False] * (n+1)
        
        DFS(graph, u, u, v, visited)
        
        # visited가 모두 True인 경우 -> 둘로 나뉘어지지 않음
        if False not in visited[1:]:
            continue
        else:
            first_cnt = visited[1:].count(True)
            second_cnt = visited[1:].count(False)
            diff = first_cnt - second_cnt
            if diff >= 0:
                diff_list.append(diff)
            else:
                diff_list.append(-diff)
    
    
    answer = min(diff_list)
    return answer