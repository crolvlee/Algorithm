N, S = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = 0
total = lst[0]
min_len = 100001

while True:
    # 1. 현재 부분합이 S보다 크거나 같은 경우
    if total >= S:
        min_len = min(min_len, end-start+1)
        total -= lst[start]
        start += 1

    # 2. 현재 부분합이 S보다 작은 경우
    elif total < S:
        end += 1
        if end == len(lst):
            break
        
        total += lst[end]

if min_len == 100001:
    print(0)
else:
    print(min_len)
