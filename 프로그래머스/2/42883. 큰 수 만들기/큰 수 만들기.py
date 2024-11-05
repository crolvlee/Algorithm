def solution(number, k):
    
    # number = 24456, k=3 -> 2와 idx 2의 4가 지워짐
    
    stack = []
    
    for num in number:
        # 현재 내 앞에 나보다 작은 숫자가 있으면 앞 숫자를 지우기
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            
        stack.append(num)
        
    if k != 0:
        stack = stack[:-k]
    
    answer = ''.join(stack)
    return answer