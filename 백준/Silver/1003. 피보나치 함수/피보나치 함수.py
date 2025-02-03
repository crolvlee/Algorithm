# dp 문제

T = int(input())
num_list = []

for _ in range(T):
    num = int(input())
    num_list.append(num)

max_num = max(num_list)

# dp 채우기 (max_num에 맞춰서)
dp_zero = [1, 0]
dp_one = [0, 1]

for i in range(2, max_num+1):
    new_zero = dp_zero[i-2] + dp_zero[i-1]
    dp_zero.append(new_zero)
    
    new_one = dp_one[i-2] + dp_one[i-1]
    dp_one.append(new_one)
    
# 출력
for n in num_list:
    print(dp_zero[n], dp_one[n])