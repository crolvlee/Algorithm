def solution(n):
    
    strn = str(n)
    
    print(strn)
    
    lst = []
    for alpha in strn:
        lst.append(int(alpha))
    

    answer = lst[::-1]
    return answer