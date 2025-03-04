from collections import deque

def can_change(word_A, word_B):
    n = len(word_A)
    different_cnt = 0
    
    for i in range(n):
        if word_A[i] == word_B[i]:
            continue
        else:
            different_cnt += 1
    
    if different_cnt == 1:
        return True
    else:
        return False

def BFS(begin, target, words, visited, n):
    q = deque([])
    q.append([begin, visited, 0])
    
    while q:
        now_word, now_visited, now_depth = q.popleft()
        
        if now_word == target:
            return now_depth
        
        for i in range(n):
            if now_visited[i] == False:
                next_word = words[i]
                if can_change(now_word, next_word) == True:
                    next_visited = now_visited[:]
                    next_visited[i] = True
                    q.append([next_word, next_visited, now_depth + 1])
            
    return 0
            
    

def solution(begin, target, words):
    n = len(words)
    visited = [False] * n
    
    answer = BFS(begin, target, words, visited, n)
    return answer