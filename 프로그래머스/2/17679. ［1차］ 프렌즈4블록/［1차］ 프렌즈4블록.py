# m: 높이
# n: 폭
# board: 배치 정보

# 비어있는 칸: @로 표시

def check_neighbor(row, col, board_list):
    if board_list[row][col] == board_list[row+1][col] and board_list[row][col] == board_list[row][col+1] and board_list[row][col] == board_list[row+1][col+1]:
        return True
    else:
        return False
    
def fall_board(m, n, board_list):
    for i in range(0, n):
        line = []   # i열에 있는 것들 (@는 제외하고)   # 예시: ['T', 'T', 'M']
        for j in range(0, m):
            if board_list[j][i] != '@':
                line.append(board_list[j][i])
        
        # i열에 있는 것을 업데이트 해주기
        # new_line 예시: ['@', '@', '@', 'T', 'T', 'M']
        at_cnt = m - len(line)
        new_line = ['@'] * at_cnt
        new_line = new_line + line
        
        for j in range(0, m):
            board_list[j][i] = new_line[j]
            
    return board_list
        
    

def solution(m, n, board):
    # 2차원 배열로 만들기
    board_list = []
    for line in board:
        line_list = []
        for alphabet in line:
            line_list.append(alphabet)
        board_list.append(line_list)
        
    
    # 지울 원소 카운트
    delete_cnt = 0
    
    # 회차별로 순회
    while True:
        delete_pos = []     # 예시: [[1, 0], [1, 1], [2, 0], [2, 1], [2, 2], ...] 
        for i in range(0, n-1):
            for j in range(0, m-1):
                if board_list[j][i] == '@':
                    continue
                if check_neighbor(j, i, board_list) == True:
                    delete_pos.append([j, i])
                    delete_pos.append([j+1, i])
                    delete_pos.append([j, i+1])
                    delete_pos.append([j+1, i+1])
                    
        # 중복되는 원소는 빼기
        new_delete_pos = []
        for delp in delete_pos:
            if delp not in new_delete_pos:
                new_delete_pos.append(delp)
        
        # delete_pos에 아무것도 없으면 while문 종료
        if len(new_delete_pos) == 0:
            break
        
        delete_cnt += len(new_delete_pos)

        #------------------------
        # 다음 단계를 위한 세팅
        # 빼는건 @로 바꿔주기
        for delp in delete_pos:
            board_list[delp[0]][delp[1]] = '@'
            
        # 아래로 떨어뜨려주기
        board_list = fall_board(m, n, board_list)


    return delete_cnt