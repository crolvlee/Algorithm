def solution(numbers):
    stack = []  # 뒷 큰 수를 찾지 못한 인덱스를 저장
    result = [-1] * len(numbers)
    
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack[-1]] = numbers[i]
            stack.pop()
        stack.append(i)
            
    
    return result