def solution(sequence):
    
    lst_A = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            now_num = sequence[i] * -1
            lst_A.append(now_num)
        else:
            now_num = sequence[i] * 1
            lst_A.append(now_num)
    
    lst_B = []
    for i in range(len(sequence)):
        if i % 2 == 0:
            now_num = sequence[i] * 1
            lst_B.append(now_num)
        else:
            now_num = sequence[i] * -1
            lst_B.append(now_num)
    
    # dp[i]: i번째 원소를 포함하면서, 가장 큰 연속되는 부분 수열의 합
    dp_A = []
    for i in range(len(lst_A)):
        if i == 0:
            dp_A.append(lst_A[i])
        else:
            now_num = max(lst_A[i], lst_A[i] + dp_A[i-1])
            dp_A.append(now_num)
    
    dp_B = []
    for i in range(len(lst_B)):
        if i == 0:
            dp_B.append(lst_B[i])
        else:
            now_num = max(lst_B[i], lst_B[i] + dp_B[i-1])
            dp_B.append(now_num)
    
    answer = max(max(dp_A), max(dp_B))
    return answer