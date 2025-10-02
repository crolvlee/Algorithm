def factorial(num):
    now_num = num
    result = 1
    
    if num == 0:
        return 1
    
    while True:
        if now_num == 1:
            break
        
        result *= now_num
        now_num -= 1

    return result


def solution(n, k):
    arr = []
    for i in range(n):
        arr.append(i+1)
        
    answer = []
    start = 0  # 이건 계속 업데이트될 예정
    
    for i in range(n):
        num = k - 1 - start
        div_num = factorial(n-1-i)
        now_idx = num // div_num
        
        # answer에 넣기 + 업데이트
        answer.append(arr[now_idx])
        arr.pop(now_idx)
        start += (now_idx * div_num)
            
    
    return answer