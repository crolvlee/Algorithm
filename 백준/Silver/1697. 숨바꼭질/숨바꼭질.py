from collections import deque

# 너비우선탐색 (BFS)
def BFS(start, end, depth, visited):
    q = deque([[start, depth]])     # [점, depth]
    
    while q:
        now_num, now_depth = q.popleft()
        
        if now_num == end:
            return now_depth
        
        next1 = now_num - 1
        next2 = now_num + 1
        next3 = now_num * 2
        
        if 0 <= next1 and next1 <= 100000:
            if visited[next1] == 0:
                q.append([next1, now_depth + 1])
                visited[next1] = 1
        if 0 <= next2 and next2 <= 100000:
            if visited[next2] == 0:
                q.append([next2, now_depth + 1])
                visited[next2] = 1
        if 0 <= next3 and next3 <= 100000:
            if visited[next3] == 0:
                q.append([next3, now_depth + 1])
                visited[next3] = 1
        

N, K = map(int, input().split())
visited = [0] * 100001
answer = BFS(N, K, 0, visited)
print(answer)
