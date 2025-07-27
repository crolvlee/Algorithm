from collections import deque

def solution(x, y, n):
    q = deque()
    q.append([x, 0])
    
    num_list = [False] * 1000001
    num_list[x] = True
    
    answer = -1
    
    while q:
        now_num, now_depth = q.popleft()
        if now_num == y:
            answer = now_depth
            break
        
        if (now_num + n) <= 1000000 and num_list[now_num + n] == False and (now_num + n) <= y:
            q.append([now_num + n, now_depth + 1])
            num_list[now_num + n] == True
            
        if (now_num * 2) <= 1000000 and num_list[now_num * 2] == False and (now_num * 2) <= y:
            q.append([now_num * 2, now_depth + 1])
            num_list[now_num * 2] = True
            
        if (now_num * 3) <= 1000000 and num_list[now_num * 3] == False and (now_num * 3) <= y:
            q.append([now_num * 3, now_depth + 1])
            num_list[now_num * 3] = True
            
    
    return answer