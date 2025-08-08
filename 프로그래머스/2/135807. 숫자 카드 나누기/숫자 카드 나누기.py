# 공약수 찾기
def common_divisor(arr):
    now_num = arr[0] # 최대 공약수
    
    # 유클리트 호제법
    for i in range(1, len(arr)):
        a = now_num
        b = arr[i]
        
        while b != 0:
            temp = a
            a = b
            b = temp % b
            
        now_num = a
    
    # 최대 공약수로 약수 찾기
    result = []
    for i in range(1, int(now_num ** 0.5) + 1):
        if now_num % i == 0:
            result.append(i)
            if i*i != now_num:
                result.append(now_num // i)
    
    return result


def solution(arrayA, arrayB):
    # 1번 경우 - arrayA는 모두 나눌 수 O / arrayB는 하나도 나눌 수 X
    result1_a = common_divisor(arrayA)
    result1_b = []
    
    for num in result1_a:
        can_divide = False
        for b in arrayB:
            if b % num == 0:
                can_divide = True
                break
        
        if can_divide == False:
            result1_b.append(num)
    
    result1_num = 0
    if result1_b:
        result1_num = max(result1_b)
    
    # 2번 경우 - arrayB는 모두 나눌 수 O / arrayA는 하나도 나눌 수 X
    result2_b = common_divisor(arrayB)
    result2_a = []
    
    for num in result2_b:
        can_divide = False
        for a in arrayA:
            if a % num == 0:
                can_divide = True
                break
        
        if can_divide == False:
            result2_a.append(num)
    
    result2_num = 0
    if result2_a:
        result2_num = max(result2_a)
    
    
    answer = max(result1_num, result2_num)
    return answer