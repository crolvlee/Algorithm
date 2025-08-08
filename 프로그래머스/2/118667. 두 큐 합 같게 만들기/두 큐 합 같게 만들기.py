from collections import deque

def solution(queue1, queue2):
    count = 0
    max_count = len(queue1) * 3 - 3
    sum_one = sum(queue1)
    sum_two = sum(queue2)
    
    dq_one = deque(queue1)
    dq_two = deque(queue2)
    
    while True:
        if count > max_count:
            count = -1
            break
            
        if sum_one == sum_two:
            break
            
        if sum_one < sum_two:
            now_num = dq_two.popleft()
            dq_one.append(now_num)
            sum_one += now_num
            sum_two -= now_num
            count += 1
        elif sum_one > sum_two:
            now_num = dq_one.popleft()
            dq_two.append(now_num)
            sum_one -= now_num
            sum_two += now_num
            count += 1
            
    answer = count
    return answer