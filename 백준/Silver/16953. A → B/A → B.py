from collections import deque

def BFS(start, goal):
    current_depth = 0
    answer = -1
    q = deque([[start, 1]])     # [현재 숫자, 깊이]

    while q:
        now = q.popleft()
        now_num = now[0]
        now_depth = now[1]
        
        # 찾은 경우
        if now_num == goal:
            answer = now_depth
            break

        # 현재 depth의 첫번째 원소일 경우
        if current_depth != now_depth:
            if now_num > goal:      # 못 찾는 것임
                break
            current_depth = now_depth

        next1 = now_num * 2
        next2 = int(str(now_num) + '1')

        if next1 <= goal:
            q.append([next1, now_depth + 1])
        if next2 <= goal:
            q.append([next2, now_depth + 1])
        
    return answer


A, B = map(int, input().split())

result = BFS(A, B)
print(result)