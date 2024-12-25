import heapq

def solution(scoville, K):
    cnt = len(scoville)
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if answer >= cnt - 1:
            answer = -1
            break
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + 2 * second
        heapq.heappush(scoville, new)
        answer += 1
        
    
    return answer