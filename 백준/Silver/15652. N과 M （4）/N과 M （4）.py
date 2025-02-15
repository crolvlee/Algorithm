import sys
sys.setrecursionlimit(10000000)

# 입력받기
N, M = map(int, input().split())

# 깊이우선탐색 DFS 함수 정의
def BFS(lst, max_num, goal):
    if len(lst) == goal:
        print(' '.join(map(str, lst)))
        return
    
    for j in range(1, max_num + 1):
        if lst[-1] <= j:
            new_lst = lst + [j]
            BFS(new_lst, max_num, goal)

# 깊이우선탐색
for i in range(1, N+1):
    BFS([i], N, M)
