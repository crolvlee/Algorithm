import math
    
def solution(n, times):
    
    start = 0
    end = max(times) * n
    
    # 이분탐색으로 가장 작은 수 확인
    answer = 0
    
    while start <= end:
        # print('-----------')
        # print('start: ', start)
        # print('end: ', end)
        mid = (start + end) // 2
        
        # 현재 수에서 심사 가능한 사람 수
        total = 0
        for now_time in times:
            total += mid // now_time
        # print('total: ', total) 
            
        if total >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
        
    
    
    return answer