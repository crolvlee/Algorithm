N = int(input())
lst = []

for _ in range(N):
    num = int(input())
    lst.append(num)

if N == 1:
    print(lst[0])
elif N == 2:
    print(lst[0] + lst[1])
elif N >= 3:
    first = lst[0]
    second = lst[0] + lst[1]
    third = max(lst[0] + lst[2], lst[1] + lst[2])
    dp = [first, second, third]

    for i in range(3, N):
        prev1 = dp[i-3] + lst[i-1] + lst[i]
        prev2 = dp[i-2] + lst[i]
        dp.append(max(prev1, prev2))
        
    print(dp[N-1])