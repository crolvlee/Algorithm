import heapq
import sys
input = sys.stdin.readline

# x가 자연수인 경우 -> 배열에 x를 추가
# x가 0인 경우 -> 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거

N = int(input().rstrip())
lst = []

for _ in range(N):
    x = int(input().rstrip())

    if x != 0:
        heapq.heappush(lst, x)
    else:
        if lst:     # 비어있지 않은 경우
            now = heapq.heappop(lst)
            print(now)
        else:       # 비어있는 경우
            print(0)
