import sys 
sys.setrecursionlimit(10000)

def DFS(maps, row, col, cnt):
    visited[row][col] = True
    current_cnt = cnt
    
    # 상
    if row - 1 >= 0 and maps[row-1][col] != 'X':
        if visited[row-1][col] == False:
            current_cnt += DFS(maps, row-1, col, int(maps[row-1][col]))
    
    # 하
    if row + 1 <= n-1 and maps[row+1][col] != 'X':
        if visited[row+1][col] == False:
            current_cnt += DFS(maps, row+1, col, int(maps[row+1][col]))
            
    # 좌
    if col - 1 >= 0 and maps[row][col-1] != 'X':
        if visited[row][col-1] == False:
            current_cnt += DFS(maps, row, col-1, int(maps[row][col-1]))
            
    # 우
    if col + 1 <= m-1 and maps[row][col+1] != 'X':
        if visited[row][col+1] == False:
            current_cnt += DFS(maps, row, col+1, int(maps[row][col+1]))
            
    return current_cnt

def solution(maps):
    
    global n
    global m
    global visited
    
    n = len(maps)       # 세로 길이
    m = len(maps[0])    # 가로 길이
    visited = [[False] * m for _ in range(n)]
    result = []
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == False:
                cnt = DFS(maps, i, j, int(maps[i][j]))
                result.append(cnt)
            else:
                continue 
    
    if len(result) == 0:
        return [-1]
    else:
        result.sort()
        return result