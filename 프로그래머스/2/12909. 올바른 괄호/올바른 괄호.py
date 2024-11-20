def solution(s):
    answer = True
    stack = []
    
    for current in s:
        if current == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
                continue
            else:
                stack.append(current)
        elif current == '(':
            stack.append(current)
        
    if stack:
        answer = False
        
    return answer