import heapq
import sys
input = sys.stdin.readline

# 입력받기
N, K = map(int, input().split())

jewels = []
for _ in range(N):
    M, V = map(int, input().split())
    jewels.append([M, V])
    
bags = []
for _ in range(K):
    C = int(input())
    bags.append(C)
    
# jewels, bags 정렬
jewels.sort() # 가방에 넣을 수 있는 무게임을 확인할 때, 앞에서부터 확인하기 위해 정렬!
bags.sort()

# 순회하면서 bag에 집어넣기
idx = 0
answer = 0
q = []

for bag in bags:
    # 현재 bag에 넣을 수 있는 보석 확인하기
    while idx < len(jewels) and jewels[idx][0] <= bag:
        heapq.heappush(q, -jewels[idx][1])    # 가격을 넣음
        idx += 1
        
    if q:
        answer += -heapq.heappop(q) # 제일 큰 가격을 뺴기

print(answer)