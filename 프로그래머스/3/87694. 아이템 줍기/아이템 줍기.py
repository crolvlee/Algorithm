# 꼭짓점에서 만나거나, 변이 겹치는 경우 없음
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    ground = [['-'] * 102 for _ in range(102)]
    
    # 테두리는 O로 표시
    for r in rectangle:
        x1, y1, x2, y2 = 2*r[0], 2*r[1], 2*r[2], 2*r[3]
        
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    ground[i][j] = 'X'
                else:
                    if ground[i][j] != 'X':
                        ground[i][j] = 'O'
        
        
    # 시작점, 끝점
    startX = 2 * characterX
    startY = 2 * characterY
    endX = 2 * itemX
    endY = 2 * itemY
    
    # BFS 함수 정의
    def BFS(startX, startY, endX, endY):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 좌우하상
        q = deque()
        visited = [[False] * 102 for _ in range(102)]
        q.append([startX, startY, 0])
        visited[startX][startY] = True
        
        while q:
            now_x, now_y, now_cnt = q.popleft()
            
            if now_x == endX and now_y == endY:
                return now_cnt // 2
            
            for d_x, d_y in directions:
                if 0 <= now_x + d_x < 102 and 0 <= now_y + d_y < 102 and ground[now_x + d_x][now_y + d_y] == 'O':
                    if visited[now_x + d_x][now_y + d_y] == False:
                        q.append([now_x + d_x, now_y + d_y, now_cnt + 1])
                        visited[now_x + d_x][now_y + d_y] = True
    
    answer = BFS(startX, startY, endX, endY)
    
    return answer
