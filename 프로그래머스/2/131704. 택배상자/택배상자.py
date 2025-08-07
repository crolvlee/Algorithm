from collections import deque

def solution(order):
    answer = 0
    main_belt = deque()
    sub_belt = []
    
    for i in range(1, len(order) + 1):
        main_belt.append(i)
        
    # order 탐색
    for now in order:
        if main_belt and main_belt[0] < now:
            while main_belt and main_belt[0] < now:
                front_num = main_belt.popleft()
                sub_belt.append(front_num)
        
        find = False
        
        if main_belt and main_belt[0] == now:
            main_belt.popleft()
            answer += 1
            find = True
        else:
            if sub_belt and sub_belt[-1] == now:
                sub_belt.pop()
                answer += 1
                find = True
        
        if find == False:
            break
    
    
    return answer