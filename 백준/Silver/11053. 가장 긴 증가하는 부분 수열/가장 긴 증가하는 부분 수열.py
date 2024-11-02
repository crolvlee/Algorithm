# 가장 긴 증가하는 부분 수열

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N     # dp[i] : A[i]를 마지막 값으로 가지는 가장 긴 증가 부분수열의 길이

# 1 2 9 5 4 5 6 7
# dp[0] = 1
# dp[1] = 2
# dp[2] = 3
# dp[3] = 3
# dp[4] = 3
# dp[5] = 4

for i in range(1, N):
    for j in range(0, i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))