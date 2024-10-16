def solution(clothes):
    my_dict = {}
    
    for cloth in clothes:
        if cloth[1] not in my_dict:
            my_dict[cloth[1]] = [cloth[0]]
        else:
            my_dict[cloth[1]].append(cloth[0])
            
    
    cnt = 1
    
    for m in my_dict:
        cnt *= (len(my_dict[m]) + 1)
    
    
    answer = cnt - 1
    return answer