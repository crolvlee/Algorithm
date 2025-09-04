from collections import deque

# 입력받기
ground = []
for _ in range(12):
    line = input()
    lst = []
    for l in line:
        lst.append(l)
    ground.append(lst)

# 상하좌우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 하나의 그룹 찾는 함수
# 그룹 안의 수가 4 이상이면 X로 바꿈
def find_group(first_row, first_col):
    visited = [[False] * 6 for _ in range(12)]
    now_color = ground[first_row][first_col]
    group_cnt = 0
    
    q = deque()
    q.append([first_row, first_col])
    visited[first_row][first_col] = True
    group_cnt += 1
    
    while q:
        now_row, now_col = q.popleft()
        for d_row, d_col in directions:
            if 0 <= now_row + d_row <= 11 and 0 <= now_col + d_col <= 5:
                if ground[now_row + d_row][now_col + d_col] == now_color:
                    if visited[now_row + d_row][now_col + d_col] == False:
                        q.append([now_row + d_row, now_col + d_col])
                        visited[now_row + d_row][now_col + d_col] = True
                        group_cnt += 1
                        
    if group_cnt >= 4:
        for i in range(12):
            for j in range(6):
                if visited[i][j] == True:
                    ground[i][j] = 'X'
        return True
    else:
        return False

# ground 갱신 함수
# 중력 영향으로 아래 떨어지게 하기
def update_ground():
    # 모든 열 상태 확인
    for i in range(0, 6):
        col_line = []  # X빼고 거꾸로 넣기
        for j in range(11, -1, -1):
            if ground[j][i] != 'X':
                col_line.append(ground[j][i])
            
        if len(col_line) < 12:
            for _ in range(12 - len(col_line)):
                col_line.append('.')
                
        for k in range(12):
            ground[11-k][i] = col_line[k]
    

answer = 0
while True:
    group_exist = False
    for i in range(12):
        for j in range(6):
            if ground[i][j] != '.' and ground[i][j] != 'X':
                if find_group(i, j) == True: # 터지는 그룹 있으면
                    group_exist = True
                    
    if group_exist == True:
        answer += 1
        
        # 다음 순회를 위해 ground 갱신
        update_ground()
        
    else:
        break
    
print(answer)