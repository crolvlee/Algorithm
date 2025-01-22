# 편의를 위해
# 내 위치 -> 0행 0열
# 상대 위치 -> n-1행 m-1열

from collections import deque

def BFS(maps, start_row, start_col, end_row, end_col):
    q = deque([[start_row, start_col, 1]])
    visited[start_row][start_col] = True
    
    while q:
        current  = q.popleft()
        now_row = current[0]
        now_col = current[1]
        cnt = current[2]
        
        if now_row == end_row and now_col == end_col:
            return cnt
        
        # 현재의 동쪽을 큐에 추가
        if now_col+1 <= end_col and maps[now_row][now_col+1] == 1:
            if visited[now_row][now_col+1] == False:
                q.append([now_row, now_col+1, cnt+1])
                visited[now_row][now_col+1] = True
                
        # 현재의 서쪽을 큐에 추가
        if now_col-1 >= 0 and maps[now_row][now_col-1] == 1:
            if visited[now_row][now_col-1] == False:
                q.append([now_row, now_col-1, cnt+1])
                visited[now_row][now_col-1] = True
        
        # 현재의 남쪽을 큐에 추가
        if now_row+1 <= end_row and maps[now_row+1][now_col] == 1:
            if visited[now_row+1][now_col] == False:
                q.append([now_row+1, now_col, cnt+1])
                visited[now_row+1][now_col] = True
                
        # 현재의 북쪽을 큐에 추가
        if now_row-1 >= 0 and maps[now_row-1][now_col] == 1:
            if visited[now_row-1][now_col] == False:
                q.append([now_row-1, now_col, cnt+1])
                visited[now_row-1][now_col] = True
                
    return -1

def solution(maps):
    n = len(maps[0])    # 가로 길이
    m = len(maps)       # 세로 길이
    
    global visited
    visited = [[False] * n for _ in range(m)]
    
    answer = BFS(maps, 0, 0, m-1, n-1)
    
    
    return answer