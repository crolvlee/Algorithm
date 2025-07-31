import math

def count_area(start_row, start_col, area_len, arr):
    cnt_1 = 0
    cnt_0 = 0
    for i in range(start_row, start_row + area_len):
        for j in range(start_col, start_col + area_len):
            if arr[i][j] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1
    
    return cnt_1, cnt_0
            

def recursion(start_row, start_col, now_len, arr):
    global cnt_1, cnt_0
    area_len = int(now_len / 2)
    
    if now_len == 1:
        return
    
    # 2사분면
    area_two_cnt_1, area_two_cnt_0 = count_area(start_row, start_col, area_len, arr)
    if area_two_cnt_1 == (area_len * area_len):
        cnt_1 -= ((area_len * area_len) - 1)
    elif area_two_cnt_0 == (area_len * area_len):
        cnt_0 -= ((area_len * area_len) - 1)
    else:
        recursion(start_row, start_col, area_len, arr)
    
    # 1사분면
    area_one_cnt_1, area_one_cnt_0 = count_area(start_row, start_col + area_len, area_len, arr)
    if area_one_cnt_1 == (area_len * area_len):
        cnt_1 -= ((area_len * area_len) - 1)
    elif area_one_cnt_0 == (area_len * area_len):
        cnt_0 -= ((area_len * area_len) - 1)
    else:
        recursion(start_row, start_col + area_len, area_len, arr)
    
    # 3사분면
    area_three_cnt_1, area_three_cnt_0 = count_area(start_row + area_len, start_col, area_len, arr)
    if area_three_cnt_1 == (area_len * area_len):
        cnt_1 -= ((area_len * area_len) - 1)
    elif area_three_cnt_0 == (area_len * area_len):
        cnt_0 -= ((area_len * area_len) - 1)
    else:
        recursion(start_row + area_len, start_col, area_len, arr)
    
    # 4사분면
    area_four_cnt_1, area_four_cnt_0 = count_area(start_row + area_len, start_col + area_len, area_len, arr)
    if area_four_cnt_1 == (area_len * area_len):
        cnt_1 -= ((area_len * area_len) - 1)
    elif area_four_cnt_0 == (area_len * area_len):
        cnt_0 -= ((area_len * area_len) - 1)
    else:
        recursion(start_row + area_len, start_col + area_len, area_len, arr)
    

def solution(arr):
    n = len(arr)
    
    global cnt_1, cnt_0
    cnt_1 = 0   # 1의 개수
    cnt_0 = 0   # 0의 개수
    
    for i in range(0, n):
        for j in range(0, n):
            if arr[i][j] == 1:
                cnt_1 += 1
            else:
                cnt_0 += 1
                
    if cnt_1 == (n * n):
        return [0, 1]
    elif cnt_0 == (n * n):
        return [1, 0]
    
    # 재귀
    recursion(0, 0, n, arr)
    
    answer = [cnt_0, cnt_1]
    return answer