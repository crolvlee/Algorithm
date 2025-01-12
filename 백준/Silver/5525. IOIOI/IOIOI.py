N = int(input())    # N: PN에서 O의 개수
M = int(input())    # M: S의 길이
S = input()         # S: 주어진 긴 문자열

answer = 0
i = 0
O_count = 0

while i < (M-1):
    if S[i:i+3] == 'IOI':
        O_count += 1
        i += 2
        
        if O_count == N:
            answer += 1
            O_count -= 1
    
    else:
        i += 1
        O_count = 0
    

print(answer)     