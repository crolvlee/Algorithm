import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = list(map(int, input().split()))

# dp 채우기
dp = [0] * (N+1)
dp[1] = num_list[0]

for i in range(2, N+1):
    dp[i] = dp[i-1] + num_list[i-1]

for _ in range(M):
    start, end = map(int, input().split())
    result = dp[end] - dp[start - 1]
    
    print(result)