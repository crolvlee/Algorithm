from collections import deque

def check(current_s):
    stack = []
    balance = True
    
    for c in current_s:
        if c == '[' or c == '(' or c == '{':
            stack.append(c)
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
        elif c == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                balance = False
                break
    
    if len(stack) == 0 and balance == True:
        return True
    else:
        return False
    

def solution(s):
    
    # s를 deque로 만들기
    lst = []
    for c in s:
        lst.append(c)
    q = deque(lst)
    

    # 만족하는거 세기
    ok_count = 0
    for _ in range(0, len(s)):
        if check(q) == True:
            ok_count += 1
        
        # ---------------
        # 다음 단계를 위해 바꿔주기
        selected = q.popleft()
        q.append(selected)
        
        
    
    return ok_count