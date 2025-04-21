import sys
input = sys.stdin.readline

N = int(input())  # N: 수열의 크기
lst = list(map(int, input().split()))

dp = [[False] * N for _ in range(N)]

# 1. s~e까지 연속된 숫자가 1개인 경우
for i in range(0, N):
    dp[i][i] = True
    
# 2. s~e까지 연속된 숫자가 2개인 경우
for i in range(1, N):
    if lst[i-1] == lst[i]:
        dp[i-1][i] = True
        

# 3. s~e까지 연속된 숫자가 3개 이상인 경우
for continue_number in range(3, N + 1):
    for start_idx in range(0, N - continue_number + 1):
        end_idx = start_idx + continue_number - 1
        
        if lst[start_idx] == lst[end_idx] and dp[start_idx + 1][end_idx - 1] == True:
            dp[start_idx][end_idx] = True


M = int(input())  # M: 질문의 개수
for _ in range(M):
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    if dp[s][e] == True:
        print(1)
    else:
        print(0)