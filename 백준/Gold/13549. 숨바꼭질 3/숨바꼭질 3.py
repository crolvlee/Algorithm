# 수빈
# 현위치 X일 때, 1초 후에 => X-1 / X+1 / 2X

# 너비우선(BFS) -> 큐
from collections import deque

def BFS(start, end):
    if start == end:
        return 0
    
    q = deque([[start, 0]])     # [숫자, 시간]
    visited = [False] * (100000 + 1) 
    answer = 0

    while True:
        now = q.popleft()
        now_num = now[0]
        now_time = now[1]

        # 다음 것
        next1 = now_num - 1
        next2 = now_num + 1
        next3 = now_num * 2

        # 다음 것 중 end가 있는 경우
        if next3 == end:
            answer = now_time
            break
        if next1 == end or next2 == end:
            answer = now_time + 1
            break

        # 다음 것 중 end가 없는 것들 처리
        if 0 <= next3 <= 100000 and visited[next3] == False:
            q.appendleft([next3, now_time])
            visited[next3] = True
        if 0 <= next1 <= 100000 and visited[next1] == False:
            q.append([next1, now_time + 1])
            visited[next1] = True
        if 0 <= next2 <= 100000 and visited[next2] == False:
            q.append([next2, now_time + 1])
            visited[next2] = True

    return answer


N, K = map(int, input().split())

time = BFS(N, K)
print(time)
