A = input()
B = input()

n_A = len(A)
n_B = len(B)

dp_str = [[""] * (n_A + 1) for _ in range(n_B + 1)]

for i in range(1, n_B + 1):
    for j in range(1, n_A + 1):
        if B[i-1] == A[j-1]:
            dp_str[i][j] = dp_str[i-1][j-1] + A[j - 1]
        else:
            if len(dp_str[i-1][j]) >= len(dp_str[i][j-1]):
                dp_str[i][j] = dp_str[i-1][j]
            else:
                dp_str[i][j] = dp_str[i][j-1]

print(len(dp_str[-1][-1]))
print(dp_str[-1][-1])