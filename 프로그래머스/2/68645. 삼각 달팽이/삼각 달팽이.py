def solution(n):
    table = [[0] * n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1,  -1)]
    
    # 1열 채우기
    for i in range(0, n):
        table[i][0] = i+1
        
    now_row = n-1
    now_col = 0
    now_num = n
    
    # 다음 열 채우기
    for j in range(1, n+1):
        move_cnt = n-j
        d_row, d_col = directions[j % 3]
        
        for k in range(0, move_cnt):
            now_row += d_row
            now_col += d_col
            table[now_row][now_col] = now_num + 1
            now_num += 1

    answer = []
    
    for line in table:
        for num in line:
            if num != 0:
                answer.append(num)
    
    return answer