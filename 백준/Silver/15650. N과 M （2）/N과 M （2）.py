# 1부터 n까지 자연수, 중복 없이 m개 고름 (조합)
n, m = map(int, input().split())

# 수열 저장
lst = []

def DFS(current, depth):
    if depth == m:
        lst.append(current)
        return
    
    for i in range(int(current[-1]) + 1, n+1):
        DFS(current + str(i), depth + 1)

DFS('0', 0)

for result in lst:
    for r in result[1:]:
        print(r, end = ' ')
    print()