from collections import deque

# 1. 기본 세팅
N, M = map(int, input().split())
cheese_real = []
for _ in range(N):
    line = list(map(str, input().split()))
    cheese_real.append(line[:])    

# 동서남북
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 2. 너비우선 BFS함수 정의
def BFS(start_row, start_col):
    q = deque()
    q.append([start_row, start_col])
    visited = [[False] * M for _ in range(N)]
    visited[start_row][start_col] = True
    cheese_real[start_row][start_col] = '-'
    
    while q:
        now_row, now_col = q.popleft()
        
        for d_row, d_col in directions:
            next_row = now_row + d_row
            next_col = now_col + d_col
            if 0 <= next_row <= N-1 and 0 <= next_col <= M-1 and visited[next_row][next_col] == False:
                if cheese_real[next_row][next_col] != '1':
                    q.append([next_row, next_col])
                    visited[next_row][next_col] = True
                    cheese_real[next_row][next_col] = '-'

# 3. 1순회 - 1시간 경과
answer = 0
while True:
    # 3-1. 이전 순회에서 녹기로 했던 2를 0으로 바꾸기
    for i in range(N):
        for j in range(M):
            if cheese_real[i][j] == '2':
                cheese_real[i][j] = '0'

    # 3-2. 바깥 공기는 '-'로 바꾸기
    BFS(0, 0)

    # 3-3. 치즈가 다 녹았는지 확인
    all_disappear = True
    for i in range(N):
        for j in range(M):
            if cheese_real[i][j] == "1":
                all_disappear = False
                break
        if all_disappear == False:
            break

    if all_disappear:
        break

    # 3-4. 바깥 공기와 접촉한 치즈는 '2'로 표시
    for i in range(N):
        for j in range(M):
            if cheese_real[i][j] == '1':
                neighbor_empty_cnt = 0
                for d_row, d_col in directions:
                    if cheese_real[i + d_row][j + d_col] == '-':
                        neighbor_empty_cnt += 1

                if neighbor_empty_cnt >= 2:
                    cheese_real[i][j] = '2'

    answer += 1
    

print(answer)
