def solution(board):
    dp = []
    
    for i, row in enumerate(board):
        dp_row = []
        for j, point in enumerate(row):
            # 현재 지점 point가 0인 경우
            if point == 0:
                dp_row.append([0, 0])
                continue
            
            # 현재 지점 point가 1인 경우
            # 1) 현재 지점 point가 첫 행이거나 첫 열인 경우
            if i == 0 or j == 0:
                dp_row.append([1, 1])
                continue
                
            # 2) 왼쪽 or 위 or 왼쪽 위가 (0, 0)인 경우 현재 point는 (1, 1)
            if board[i][j-1] == 0 or board[i-1][j] == 0 or board[i-1][j-1] == 0:
                dp_row.append([1, 1])
                continue
                
            # 3) 그 외 경우
            min_num = min(dp_row[-1][0], dp[i-1][j][0], dp[i-1][j-1][0])
            dp_row.append([min_num + 1, min_num + 1])
        
        dp.append(dp_row)
    
    # dp 테이블을 탐색
    max_num = -1
    for d in dp:
        for p in d:
            if max_num < p[0]:
                max_num = p[0]
                
    return max_num * max_num