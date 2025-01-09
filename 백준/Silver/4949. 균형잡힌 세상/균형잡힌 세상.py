# 입력받기
while True:
    current_line = input()
    if current_line == '.':
        break
    
    # 점검해주기
    stack = []
    
    # 균형잡힌건지 확인
    balance = True
    
    for c in current_line:
        # 1. 여는 것은 그냥 추가
        if c == '[' or c== '(':
            stack.append(c)
            
        # 2. 닫는 것은 점검해주기
        elif c == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                balance = False
                break
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                balance = False
                break
        else:
            continue
        
    if balance == True and len(stack) == 0:
        print('yes')
    else:
        print('no')
            