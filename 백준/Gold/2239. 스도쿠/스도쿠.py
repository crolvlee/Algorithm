import copy

# 현재 칸에서 가능한 숫자
def possibleNum(now_row, now_col):
    candidate_dict = {}     # 0부터 시작하니, 나중에 그거 고려하기!
    for i in range(0, 10):
        candidate_dict[str(i)] = True
    
    # 1. 같은 행에 있는 것 찾기
    for j in range(9):
        candidate_dict[ground[now_row][j]] = False
        
    # 2. 같은 열에 있는 것 찾기
    for k in range(9):
        candidate_dict[ground[k][now_col]] = False
        
    # 3. 같은 사각형에 있는 것 찾기
    # 3-1. 1번 사각형
    if now_row in [0, 1, 2] and now_col in [0, 1, 2]:
        for i in range(0, 3):
            for j in range(0, 3):
                candidate_dict[ground[i][j]] = False
    # 3-2. 2번 사각형
    elif now_row in [0, 1, 2] and now_col in [3, 4, 5]:
        for i in range(0, 3):
            for j in range(3, 6):
                candidate_dict[ground[i][j]] = False
    # 3-3. 3번 사각형
    elif now_row in [0, 1, 2] and now_col in [6, 7, 8]:
        for i in range(0, 3):
            for j in range(6, 9):
                candidate_dict[ground[i][j]] = False
    # 3-4. 4번 사각형
    elif now_row in [3, 4, 5] and now_col in [0, 1, 2]:
        for i in range(3, 6):
            for j in range(0, 3):
                candidate_dict[ground[i][j]] = False
    # 3-5. 5번 사각형
    elif now_row in [3, 4, 5] and now_col in [3, 4, 5]:
        for i in range(3, 6):
            for j in range(3, 6):
                candidate_dict[ground[i][j]] = False
    # 3-6. 6번 사각형
    elif now_row in [3, 4, 5] and now_col in [6, 7, 8]:
        for i in range(3, 6):
            for j in range(6, 9):
                candidate_dict[ground[i][j]] = False
    # 3-7. 7번 사각형
    elif now_row in [6, 7, 8] and now_col in [0, 1, 2]:
        for i in range(6, 9):
            for j in range(0, 3):
                candidate_dict[ground[i][j]] = False
    # 3-8. 8번 사각형
    elif now_row in [6, 7, 8] and now_col in [3, 4, 5]:
        for i in range(6, 9):
            for j in range(3, 6):
                candidate_dict[ground[i][j]] = False
    # 3-9. 9번 사각형
    elif now_row in [6, 7, 8] and now_col in [6, 7, 8]:
        for i in range(6, 9):
            for j in range(6, 9):
                candidate_dict[ground[i][j]] = False
    
    result = []
    for k, v in candidate_dict.items():
        if v == True and k != 0:
            result.append(k)
            
    return result


# # 깊이우선 DFS
def DFS(pos_idx):
    global find
    if find == True:
        return
    
    if pos_idx == len(zero_pos):
        global answer_ground
        answer_ground = copy.deepcopy(ground)
        find = True
        return

    # 가능한 숫자 중 작은 것을 ground에 넣고, 해제
    now_row, now_col = zero_pos[pos_idx]
    possible_num_list = possibleNum(now_row, now_col)

    for possible_num in possible_num_list:
        ground[now_row][now_col] = possible_num
        DFS(pos_idx + 1)
        ground[now_row][now_col] = "0"


# ========================
# ground 배열
global ground
ground = []

# 0의 위치 배열
global zero_pos
zero_pos = []

for i in range(9):
    line = input()
    new_row = []
    for a in line:
        new_row.append(a)
    ground.append(new_row)

    for j in range(9):
        if line[j] == '0':
            zero_pos.append((i, j))

# DFS로 answer_ground 찾기
answer_ground = []
find = False
DFS(0)

for i in range(9):
    line = answer_ground[i]
    print("".join(line))