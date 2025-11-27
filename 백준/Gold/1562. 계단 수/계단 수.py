N = int(input())

# 1. dp 초기화
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]
# dp[x][y][z]: 자릿수 x일 때, 끝 수가 y일 경우, 비트 z에 해당하는 숫자의 경우의 수

for k in range(1, 10):
    dp[1][k][1 << k] = 1

# 2. dp 채우기
for i in range(2, N+1):       # i: 자릿수
    for j in range(0, 10):  # j: 끝 수
        for bit in range(1024):
            new_bit = bit | (1 << j)
            
            if j-1 >= 0:
                dp[i][j][new_bit] += dp[i-1][j-1][bit]
            if j+1 <= 9:
                dp[i][j][new_bit] += dp[i-1][j+1][bit]
                
            dp[i][j][new_bit] %= 1_000_000_000

# 3. 답 구하기
answer = 0
for a in range(0, 10):
    answer += dp[N][a][1023]
    answer %= 1_000_000_000

print(answer)
