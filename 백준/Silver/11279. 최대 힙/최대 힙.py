import sys
import heapq
input = sys.stdin.readline

N = int(input())
q = []
heapq.heapify(q)

for _ in range(N):
    num = int(input())
    
    # 1. 현재 수가 0
    if num == 0:
        if len(q) == 0:
            print(0)
        else:
            max_num = -heapq.heappop(q)
            print(max_num)
    
    # 2. 현재 수가 0 아님
    else:
        heapq.heappush(q, -num)
        
