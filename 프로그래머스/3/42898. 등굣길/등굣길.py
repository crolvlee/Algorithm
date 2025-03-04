# 편의상 (0, 0)에서 (m-1, n-1)로 가는 것으로 하겠음
# puddles에 저장된 좌푯값도 보정 필요


def solution(m, n, puddles):
    dp = [[-1] * m for _ in range(n)]
    
    for p in puddles:
        p_col = p[0] - 1
        p_row = p[1] - 1
        
        dp[p_row][p_col] = 0
        
    # 0행과 0열은 1로 채우기
    p_found = False
    for a in range(m):
        if p_found == False:
            if dp[0][a] != 0:
                dp[0][a] = 1
            else:
                dp[0][a] = 0
                p_found = True
        elif p_found == True:
            dp[0][a] = 0
            
    p_found = False
    for b in range(n):
        if p_found == False:
            if dp[b][0] != 0:
                dp[b][0] = 1
            else:
                dp[b][0] = 0
                p_found = True
        elif p_found == True:
            dp[b][0] = 0    
    
    print(dp)
    
    # dp 마저 채우기
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == 0:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        
    answer = (dp[n-1][m-1]) % 1000000007
    return answer