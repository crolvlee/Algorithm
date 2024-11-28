# DFS 함수 정의
def DFS(depth, result, visited):
    if depth == M:
        # print(result)
        print(' '.join(map(str, result)))
        return
    
    prev = -1
    for i in range(N):
        if visited[i] == False and lst[i] != prev:
            visited[i] = True
            new_result = result + [lst[i]]
            DFS(depth + 1, new_result, visited)
            visited[i] = False
            prev = lst[i]
                
# N: lst의 개수, M: 뽑을 숫자의 개수
N, M = map(int, input().split())
lst = list(map(int, input().split()))   # lst의 길이는 N개
lst.sort()
result = []
visited  = [False] * N
 
DFS(0, result, visited)