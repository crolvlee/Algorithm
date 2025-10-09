# 입력받기
N = int(input())
lst = list(map(int, input().split()))
lst.sort()

answer = 0

for i in range(N):
    # 투포인터
    s_idx = 0
    e_idx = N-1
    
    while s_idx < e_idx:
        if lst[s_idx] + lst[e_idx] == lst[i]:
            if s_idx == i:
                s_idx += 1
            elif e_idx == i:
                e_idx -= 1
            else:
                answer += 1
                break
        elif lst[s_idx] + lst[e_idx] < lst[i]:
            s_idx += 1
        elif lst[s_idx] + lst[e_idx] > lst[i]:
            e_idx -= 1
            
print(answer)