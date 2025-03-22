N = int(input())
A = list(map(int, input().split()))
A_reversed = A[::-1]

dp_left = [1] * N
dp_right = [1] * N

for i in range(0, N):
    for j in range(0, i):
        if A[i] > A[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)
            
for i in range(0, N):
    for j in range(0, i):
        if A_reversed[i] > A_reversed[j]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)
            
dp_right = dp_right[::-1]

result = 0
# 가장 긴 것 찾기
for i in range(N):
    a = dp_left[i]
    b = dp_right[i]
    
    result = max(result, a + b)
    
print(result - 1)