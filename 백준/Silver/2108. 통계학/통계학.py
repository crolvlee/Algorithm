import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    num = int(input())
    lst.append(num)

# 1. 산술평균
a = round(sum(lst) / N, 0)
print(int(a))

# 2. 중앙값
sorted_lst = sorted(lst)
b = sorted_lst[N//2]
print(b)

# 3. 최빈값
lst_dict = {}
for num in sorted_lst:
    if num not in lst_dict:
        lst_dict[num] = 1
    else:
        lst_dict[num] += 1

max_count = 0
for k, v in lst_dict.items():
    if v >= max_count:
        max_count = v

max_count_num = []    
for k, v in lst_dict.items():
    if v == max_count:
        max_count_num.append(k)

if len(max_count_num) == 1:
    print(max_count_num[0])
else:
    max_count_num.sort()
    print(max_count_num[1])

# 4. 범위
max_num = sorted_lst[-1]
min_num = sorted_lst[0]
print(max_num - min_num)
