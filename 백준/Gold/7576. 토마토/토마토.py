from collections import deque

def isZeroExist(table):
    isZeroExist = False
    
    for a in range(N):
        for b in range(M):
            if table[a][b] == 0:
                isZeroExist = True
                break
    
    return isZeroExist

# 너비우선 BFS 문제!
def BFS(box, M, N):
    q = deque([])
    
    # 처음부터 모두 익은지 확인
    if isZeroExist(box) == False:
        return 0
    
    # 초기 큐 세팅
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                q.append([i, j, 0])    # [행 번호, 열 번호, 날짜]
        
    days_count = 0
            
    while q:
        now_row, now_col, now_days = q.popleft()
        if now_days > days_count:
            days_count = now_days
        
        # 아랫쪽
        if now_row + 1 <= N - 1:
            if box[now_row + 1][now_col] == 0:
                box[now_row + 1][now_col] = 1
                q.append([now_row + 1, now_col, now_days + 1])
        
        # 윗쪽
        if now_row - 1 >= 0:
            if box[now_row - 1][now_col] == 0:
                box[now_row - 1][now_col] = 1
                q.append([now_row - 1, now_col, now_days + 1])
                
        # 왼쪽
        if now_col - 1 >= 0:
            if box[now_row][now_col - 1] == 0:
                box[now_row][now_col - 1] = 1
                q.append([now_row, now_col - 1, now_days + 1])
                
        # 오른쪽
        if now_col + 1 <= M - 1:
            if box[now_row][now_col + 1] == 0:
                box[now_row][now_col + 1] = 1
                q.append([now_row, now_col + 1, now_days + 1])
    
    # 탐색 다 끝낸 후 0이 남아있는지 확인
    if isZeroExist(box) == True:
        return -1
    else:
        return days_count


M, N = map(int, input().split())
box = []
for _ in range(N):
    line = list(map(int, input().split()))
    box.append(line)

answer = BFS(box, M, N)
print(answer)