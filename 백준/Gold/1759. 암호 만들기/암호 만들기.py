# 입력받기
L, C = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()

# 조합 만드는 함수
def make_combi(lst, k):
    result = []
    path = []
    
    def DFS(start_idx, depth):
        if depth == k:
            result.append(path[:])
            return
        
        for i in range(start_idx, len(lst)):
            path.append(lst[i])
            DFS(i + 1, depth + 1)
            path.pop()
        
        
    DFS(0, 0)
    return result
    
combis = make_combi(lst, L)

# 모음, 자음 개수
for com in combis:
    mo_cnt = 0
    ja_cnt = 0
    
    for alphabet in com:
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            mo_cnt += 1
        else:
            ja_cnt += 1
            
    if mo_cnt < 1 or ja_cnt < 2:
        continue
    else:
        print(''.join(com))
    
    