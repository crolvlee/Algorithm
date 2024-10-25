def solution(n):
    
    result = ''
    
    while n > 0:
        if n % 3 == 1:
            result = '1' + result
            n -= 1
        elif n % 3 == 2:
            result = '2' + result
            n -= 2
        elif n % 3 == 0:
            result = '4' + result
            n -= 3
            
        n = n // 3
    
    return result