# 입력받기
N, r, c = map(int, input().split())

answer = 0

while N != 0:
    # 현재 위치 2사분면
    if r < 2 ** (N-1) and c < 2 ** (N-1):
        answer += (2 ** (N-1)) * (2 ** (N-1)) * 0
    
    # 현재 위치 1사분면
    elif r < 2 ** (N-1) and c >= 2 ** (N-1):
        answer += (2 ** (N-1)) * (2 ** (N-1)) * 1
        c -= 2**(N-1)
    
    # 현재 위치 3사분면
    elif r >= 2 ** (N-1) and c < 2 ** (N-1):
        answer += (2 ** (N-1)) * (2 ** (N-1)) * 2
        r -= 2**(N-1)
        
    # 현재 위치가 4사분면
    else:
        answer += (2 ** (N-1)) * (2 ** (N-1)) * 3
        r -= 2**(N-1)
        c -= 2**(N-1)
        
    N -= 1

print(answer)