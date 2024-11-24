# 중위표기 -> 후위표기
def in_to_post(expression_list, priority):
    first = priority[0]
    second = priority[1]
    third = priority[2]
    stack = []  # 연산자 넣는 스택. 현재 탐색하는 연산자보다 우선순위 높거나 같은건 꺼내기
    new_expression = []
    
    for e in expression_list:
        # 현재 탐색 중인게 피연산자인 경우
        if e not in '+-*':
            new_expression.append(e)
            continue
        
        # 현재 탐색 중인게 연산자인 경우
        if e == first:
            while stack and stack[-1] == first:
                x = stack.pop(-1)
                new_expression.append(x)
        elif e == second:
            while stack and (stack[-1] == first or stack[-1] == second):
                x = stack.pop(-1)
                new_expression.append(x)
        elif e == third:
            while stack and (stack[-1] == first or stack[-1] == second or stack[-1] == third):
                x = stack.pop(-1)
                new_expression.append(x)
        stack.append(e)
    
    while stack:
        new_expression.append(stack.pop())
    
    return new_expression

# 후위표기 계산
def calculate_post(new_expression):
    stack = []
    
    for e in new_expression:
        # 현재 탐색 중인게 피연산자인 경우
        if e not in '+-*':
            stack.append(int(e))
            continue
        
        # 현재 탐생 중인게 연산자인 경우
        if e == '+':
            back = stack.pop()
            front = stack.pop()
            stack.append(front + back)
        elif e == '-':
            back = stack.pop()
            front = stack.pop()
            stack.append(front - back)
        elif e == '*':
            back = stack.pop()
            front = stack.pop()
            stack.append(front * back)
    
    return stack[0]
            

def solution(expression):
    priority_list = ['+-*', '+*-', '-+*', '-*+', '*+-', '*-+']
    expression_list = []
    tmp_num = ''
    for e in expression:
        if e not in '+-*':
            tmp_num += e
        elif e in '+-*':
            expression_list.append(tmp_num)
            tmp_num = ''
            expression_list.append(e)
    expression_list.append(tmp_num)
    
    result_list = []
    for priority in priority_list:
        new_expression = in_to_post(expression_list, priority)
        result = calculate_post(new_expression)
        if result >= 0:
            result_list.append(result)
        elif result < 0:
            result_list.append(-result)
    
    answer = max(result_list)
    return answer