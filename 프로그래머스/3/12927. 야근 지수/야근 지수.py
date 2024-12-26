# 1 1 1 1
# 0 1 1 1 (1번)
# 0 0 1 1 (2번)
# 0 0 0 1 (3번)


import heapq

def solution(n, works):
    answer = 0
    works_heap = []
    
    for w in works:
        heapq.heappush(works_heap, -w)  # [-1, -1, -1, -1]
    
    for i in range(n):
        if works_heap[0] == 0:
             break
        selected = heapq.heappop(works_heap)
        heapq.heappush(works_heap, selected + 1)
        
    # answer 계산
    if works_heap[0] == 0:
        answer = 0
    else:
        for w in works_heap:
            answer += w * w    
    
    return answer