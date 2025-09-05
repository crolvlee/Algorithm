# 입력받기
N, M = map(int, input().split())
lst = []
for _ in range(N):
    money = int(input())
    lst.append(money)

# 이분탐색
left = max(lst)
right = sum(lst)

while True:
    if left > right:
        break
    
    mid = (left + right) // 2
    
    holding_money = 0
    group_cnt = 0  # 현재 mid로 만들 수 있는 그룹 수의 최솟값
    
    for today_money in lst:
        if holding_money <= today_money:  # 돈 인출해야 하는 경우
            holding_money = mid
            group_cnt += 1
            holding_money -= today_money
        else:   # 돈 인출 안 하는 경우
            holding_money -= today_money
            
    # 현재 mid로 만들 수 있는 그룹 수의 최솟값이 M보다 크면
    if group_cnt > M:
        left = mid + 1
    else:
        right = mid - 1
        
print(mid)