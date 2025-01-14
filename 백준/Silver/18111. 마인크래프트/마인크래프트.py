# 이분탐색
import sys
input = sys.stdin.readline

# 입력받기
N, M, B = map(int, input().split())
ground = []

for _ in range(N):
    line = list(map(int, input().split()))
    ground += line
    
min_num = min(ground)
max_num = max(ground)

result_time = 1e9
result_height = 0

# 특정 높이일 때, 시간이 얼마 소요되는지
result = []     # [시간, 높이]  # 나중에 시간은 오름차순, 높이는 내림차순 해야 함

for i in range(min_num, max_num+1):     # i는 특정 높이
    add_block = 0       # 땅에 추가     / 인벤토리에서 뺌
    remove_block = 0    # 땅에서 제거   / 인벤토리에 넣음
    
    for g in ground:
        if g > i:
            remove_block += (g-i)
        elif g < i:
            add_block += (i-g)
            
    if remove_block + B >= add_block:
        time = (add_block * 1) + (remove_block * 2)
        if result_time >= time:
            result_time = time
            result_height = i
            
print(result_time, result_height)