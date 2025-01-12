N = int(input())    # N: PN에서 O의 개수
M = int(input())    # M: S의 길이
S = input()         # S: 주어진 긴 문자열

answer = 0


for idx, s in enumerate(S):
    if s == 'O':
        continue
    
    current = 'I'    # 글자 업데이트 될 예정. ex. IOI
    O_count = 0
    now_idx = idx + 1

    while now_idx < len(S):
        if current[-1] == S[now_idx]:
            break
        else:
            current += S[now_idx]
            if S[now_idx] == 'O':
                O_count += 1
        
        now_idx += 1
        
        if O_count == N and current[-1] == 'I':
            answer += 1
            break

print(answer)