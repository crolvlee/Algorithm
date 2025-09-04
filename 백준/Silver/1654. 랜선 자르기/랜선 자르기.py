# 입력받기
K, N = map(int, input().split())
lst = []
for _ in range(K):
    num = int(input())
    lst.append(num)

# 만들 수 있는 랜선 개수 확인하는 함수
def check_cnt(now_len):
    result = 0
    for num in lst:
        result += (num // now_len)
    
    return result

# 이분탐색
left = 1
right = max(lst)
now_num = 0

while True:
    if left > right:
        break
    
    mid = (left + right) // 2
    
    if check_cnt(mid) < N:
        right = mid - 1
    elif check_cnt(mid) > N:
        now_num = mid
        left = mid + 1
    elif check_cnt(mid) == N:
        now_num = mid
        left = mid + 1

print(now_num)