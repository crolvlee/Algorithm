# 이동은 상, 하, 좌, 우 중에서 한 방향으로만
# 장애물 전까지 가는 것 - 한 번의 이동으로 침!

# R: 로봇의 처음 위치
# D: 장애물 위치
# G: 도착점 위치

# 가는 도중 장애물에 부딪혔을 때, 두 방향으로 갈 수 있음 (그 두 방향 가는 길이 있다고 가정했을 때)

# BFS 문제!

from collections import deque

def BFS(board_list, R_pos, G_pos):
    pos_q = deque([R_pos + [0]])      # 예시: pos_q: [[2, 7, 1], [1, 5, 1]]   # [행, 열, 카운트]
    move_cnt = 0
    visited = [R_pos]
    find = False
    
    while pos_q:
        now_pos = pos_q.popleft()   # 예시: now_pos = [1, 7]      # 1행 7열
        now_row = now_pos[0]
        now_col = now_pos[1]
        now_cnt = now_pos[2]
        
        print(now_pos)
        print("----------")

        # 1. 위쪽으로 이동
        updated_up_row = now_row
        while board_list[updated_up_row-1][now_col] != 'D':
            updated_up_row -= 1
            
        if board_list[updated_up_row][now_col] == 'G':
            move_cnt = now_cnt + 1
            find = True
            break

        if updated_up_row != now_row and [updated_up_row, now_col] not in visited:
            pos_q.append([updated_up_row, now_col, now_cnt + 1])
            visited.append([updated_up_row, now_col])
            print("윗쪽 업데이트!")

        # 2. 오른쪽으로 이동
        updated_right_col = now_col
        while board_list[now_row][updated_right_col+1] != 'D':
            updated_right_col += 1
            
        if board_list[now_row][updated_right_col] == 'G':
            move_cnt = now_cnt + 1
            find = True
            break

        if updated_right_col != now_col and [now_row, updated_right_col] not in visited:
            pos_q.append([now_row, updated_right_col, now_cnt + 1])
            visited.append([now_row, updated_right_col])
            print("오른쪽 업데이트!")

        # 3. 아래쪽으로 이동
        updated_down_row = now_row
        while board_list[updated_down_row+1][now_col] != 'D':
            updated_down_row += 1
            
        if board_list[updated_down_row][now_col] == 'G':
            move_cnt = now_cnt + 1
            find = True
            break

        if updated_down_row != now_row and [updated_down_row, now_col] not in visited:
            pos_q.append([updated_down_row, now_col, now_cnt + 1])
            visited.append([updated_down_row, now_col])
            print("아래쪽 업데이트!")
            

        # 4. 왼쪽으로 이동
        updated_left_col = now_col
        while board_list[now_row][updated_left_col-1] != 'D':
            updated_left_col -= 1
            
        if board_list[now_row][updated_left_col] == 'G':
            move_cnt = now_cnt + 1
            find = True
            break

        if updated_left_col != now_col and [now_row, updated_left_col] not in visited:
            pos_q.append([now_row, updated_left_col, now_cnt + 1])
            visited.append([now_row, updated_left_col])
            print("왼쪽 업데이트!")
            
    if find == True:
        return move_cnt
    else:
        return -1


def solution(board):
    
    # 새로운 board_list 만들기 / D, G위치 기억하기
    board_list = []
    R_pos = []
    G_pos = []
    
    new_line_cnt = len(board[0]) + 2
    board_list.append(['D'] * new_line_cnt)
    
    for row, line in enumerate(board):
        new_line = ['D']
        for col, block in enumerate(line):
            new_line.append(block)
            
            if block == 'R':
                R_pos = [row+1, col+1]
            if block == 'G':
                G_pos = [row+1, col+1]
        new_line.append('D')
        board_list.append(new_line)
    
    board_list.append(['D'] * new_line_cnt)
    
    # BFS 탐색하기
    answer =  BFS(board_list, R_pos, G_pos)
    return answer