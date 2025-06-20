# 조합 문제!

def combi(n, k):
    global combi_list
    visited = [False] * n
    path = []
    
    def DFS(start, depth):
        if depth == k:
            combi_list.append(path[:])
            return
        
        for i in range(start, n):
            if visited[i] == False:
                path.append(i)
                visited[i] = True
                DFS(i + 1, depth + 1)
                path.pop()
                visited[i] = False
        
    DFS(0, 0)        

def solution(relation):
    # n: 행의 개수, m: 열의 개수
    n = len(relation)
    m = len(relation[0])
    
    # 조합 인덱스
    global combi_list
    combi_list = []
    
    for i in range(1, m+1):
        combi(m, i)
        
    # 조합 돌면서 후보키로 가능한 것 찾기
    candidate_list = []
    
    for com in combi_list:
        # 1. 유일성 확인
        contents = set()
        
        for line in relation:
            now_content = []
            for num in com:
                now_content.append(line[num])
            
            contents.add(tuple(now_content))
        
        if len(contents) != n:
            continue
        
        # 2. 최소성 확인
        minimal = True
        for candidate in candidate_list:
            # candidate가 com의 부분집합인지 확인
            include_cnt = 0
            for idx in candidate:
                if idx in com:
                    include_cnt += 1
            
            if include_cnt == len(candidate):
                minimal = False
                
        if minimal == True:
            candidate_list.append(com)
        
        
    answer = len(candidate_list)
    return answer