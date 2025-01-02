def solution(routes):
    routes.sort(key=lambda x:x[1])
    answer = 0
    current_point = -1e9
    
    for route in routes:
        if current_point < route[0] or route[1] < current_point:
            current_point = route[1]
            answer += 1
        else:
            continue
        
        
    
    return answer