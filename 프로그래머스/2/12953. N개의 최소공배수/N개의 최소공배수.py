def solution(arr):
    min_lcm = max(arr)
    max_lcm = 1
    for a in arr:
        max_lcm *= a
    
    lcm = 0
    for i in range(min_lcm, max_lcm + 1):
        is_lcm = True
        for a in arr:
            if i % a == 0:
                continue
            else:
                is_lcm = False
                break
        
        if is_lcm == True:
            lcm = i
            break
                
                
    return lcm