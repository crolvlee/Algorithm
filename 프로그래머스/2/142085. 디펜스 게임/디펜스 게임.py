def solution(n, k, enemy):
    start = 0
    end = len(enemy)
    
    while start < end:
        mid = (start + end) // 2
        
        now_enemy = enemy[0:mid+1]
        now_enemy.sort()
        now_sum = sum(now_enemy[0:-k])
        
        if now_sum <= n:
            start = mid + 1
        else:
            end = mid
            
            
    answer = start
    return answer