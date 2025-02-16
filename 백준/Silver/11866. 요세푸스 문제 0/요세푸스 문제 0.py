# 입력받음
N, K = map(int, input().split())
lst = []

for i in range(1, N+1):
    lst.append(i)

# 순회하면서 배열 찾기
result = []
idx = 0

while len(result) != N:
    now_cnt = 0
    while True:
        if lst[idx] != -1:
            now_cnt += 1
        
        if now_cnt == K:
            break
        
        # 다음 인덱스
        idx = (idx + 1) % N
        

    result.append(lst[idx])
    lst[idx] = -1
    idx = (idx + 1) % N

print('<' + ', '.join(map(str, result)) + '>')