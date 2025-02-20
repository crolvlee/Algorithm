import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
from collections import deque

def BFS(start, goal, visited, command):
    q = deque([[start, command]])     # [숫자, 지금까지의 명령어]. 여기 들어가는 숫자는 문자열 형태!

    while q:
        now_num, now_command = q.popleft()    # now_num은 문자열 형태

        if int(now_num) == int(goal):
            return now_command

        # 1. D
        next_d = str((int(now_num) * 2) % 10000)
        if len(next_d) == 1:
            next_d = '000' + next_d
        elif len(next_d) == 2:
            next_d = '00' + next_d
        elif len(next_d) == 3:
            next_d = '0' + next_d
        
        if visited[int(next_d)] == 0:
            q.append([next_d, now_command + "D"])
            visited[int(next_d)] = 1

        # 2. S
        if int(now_num) == 0:
            next_s = str(9999)
        else:
            next_s = str(int(now_num) - 1)
        
        if len(next_s) == 1:
            next_s = '000' + next_s
        elif len(next_s) == 2:
            next_s = '00' + next_s
        elif len(next_s) == 3:
            next_s = '0' + next_s            
            
        if visited[int(next_s)] == 0:
            q.append([next_s, now_command + "S"])
            visited[int(next_s)] = 1

        # 3. L
        next_l = now_num[1:] + now_num[0]
        if visited[int(next_l)] == 0:
            q.append([next_l, now_command + "L"])
            visited[int(next_l)] = 1

        # 4. R
        next_r = now_num[-1] + now_num[:-1]
        if visited[int(next_r)] == 0:
            q.append([next_r, now_command + "R"])
            visited[int(next_r)] = 1


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = 1

    A = str(A)
    if len(str(A)) == 3:
        A = '0' + A
    elif len(str(A)) == 2:
        A = '00' + A
    elif len(str(A)) == 1:
        A = '000' + A

    B = str(B)
    if len(str(B)) == 3:
        B = "0" + B
    elif len(str(A)) == 2:
        B = "00" + B
    elif len(str(A)) == 1:
        B = "000" + B

    result = BFS(A, B, visited, '')
    print(result)
