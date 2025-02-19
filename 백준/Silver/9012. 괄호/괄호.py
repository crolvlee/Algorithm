N = int(input())

for _ in range(N):
    stack = []
    input_str = input()
    
    for s in input_str:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)
                
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')