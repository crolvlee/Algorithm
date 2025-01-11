N, K = map(int, input().split())
num_list = []

for _ in range(N):
    num = int(input())
    num_list.append(num)
    
num_list.sort(reverse=True)
    
current_num = 0
coin_cnt = 0

for num in num_list:
    if num > K:
        continue
    
    share = (K - current_num) // num
    current_num += num * share
    coin_cnt += share
    
    if current_num == K:
        break
    
print(coin_cnt)