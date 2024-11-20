def solution(a, b):
    small = min(a, b)
    big = max(a, b)
    hab = 0
    
    for i in range(small, big+1):
        hab += i
    
    return hab