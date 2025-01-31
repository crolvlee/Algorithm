import sys
input = sys.stdin.readline

N = int(input())
input_list = list(map(int, input().split()))
sorted_set_list = sorted(list(set(input_list)))

num_dict = {}   # 예시. {999: 0, 1000: 1}

for i, num in enumerate(sorted_set_list):
    num_dict[num] = i
    
for k in input_list:
    print(num_dict[k], end =' ')