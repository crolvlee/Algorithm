from collections import deque

def BFS(maps, s_row, s_col, e_row, e_col, n, m):
    # 동서남북
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # visited, q
    visited = [[False] * m for _ in range(n)]
    visited[s_row][s_col] = True
    q = deque([[s_row, s_col, 0]])
    
    # result는 업데이트 될 예정
    result = -1
    
    while q:
        now_row, now_col, now_dist = q.popleft()
        
        if now_row == e_row and now_col == e_col:
            result = now_dist
            break
            
        for d_row, d_col in directions:
            if 0 <= now_row + d_row <= n-1 and 0 <= now_col + d_col <= m-1 and visited[now_row + d_row][now_col + d_col] == False and maps[now_row + d_row][now_col + d_col] != 'X':
                q.append([now_row + d_row, now_col + d_col, now_dist + 1])
                visited[now_row + d_row][now_col + d_col] = True
                    
    return result
    


def solution(maps):
    
    # 세로, 가로 길이
    n = len(maps)
    m = len(maps[0])
    
    # 위치 찾기
    s_row = 0
    s_col = 0
    l_row = 0
    l_col = 0
    e_row = 0
    e_col = 0
    find_cnt = 0
    
    for i in range(n):
        if find_cnt == 3:
            break
            
        for j in range(m):
            if find_cnt == 3:
                break
                
            if maps[i][j] == 'S':
                s_row = i
                s_col = j
                find_cnt += 1
            elif maps[i][j] == 'L':
                l_row = i
                l_col = j
                find_cnt += 1
            elif maps[i][j] == 'E':
                e_row = i
                e_col = j
                find_cnt += 1
    
    # ======
    
    # 1. S -> L
    first_dist = BFS(maps, s_row, s_col, l_row, l_col, n, m)
    if first_dist == -1:
        return -1
    
    # 2. L -> E
    second_dist = BFS(maps, l_row, l_col, e_row, e_col, n, m)
    if second_dist == -1:
        return -1
    
    answer = first_dist + second_dist
    return answer