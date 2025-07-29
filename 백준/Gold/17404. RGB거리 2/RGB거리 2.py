# 입력받기
N = int(input())
lst = []
for _ in range(N):
    line = list(map(int, input().split()))
    lst.append(line)

# R로 시작한 것
start_with_R = [0, lst[0][0] + lst[1][1], lst[0][0] + lst[1][2]]

for i in range(2, N):
    next_R_candidate = []
    next_G_candidate = []
    next_B_candidate = []

    if start_with_R[0] != 0:
        R_B = start_with_R[0] + lst[i][2]
        R_G = start_with_R[0] + lst[i][1]
        next_B_candidate.append(R_B)
        next_G_candidate.append(R_G)

    if start_with_R[1] != 0:
        G_R = start_with_R[1] + lst[i][0]
        G_B = start_with_R[1] + lst[i][2]
        next_R_candidate.append(G_R)
        next_B_candidate.append(G_B)

    if start_with_R[2] != 0:
        B_R = start_with_R[2] + lst[i][0]
        B_G = start_with_R[2] + lst[i][1]
        next_R_candidate.append(B_R)
        next_G_candidate.append(B_G)

    start_with_R[0] = min(next_R_candidate)
    start_with_R[1] = min(next_G_candidate)
    start_with_R[2] = min(next_B_candidate)

# G로 시작한 것
start_with_G = [lst[0][1] + lst[1][0], 0, lst[0][1] + lst[1][2]]

for i in range(2, N):
    next_R_candidate = []
    next_G_candidate = []
    next_B_candidate = []

    if start_with_G[0] != 0:
        R_B = start_with_G[0] + lst[i][2]
        R_G = start_with_G[0] + lst[i][1]
        next_B_candidate.append(R_B)
        next_G_candidate.append(R_G)

    if start_with_G[1] != 0:
        G_R = start_with_G[1] + lst[i][0]
        G_B = start_with_G[1] + lst[i][2]
        next_R_candidate.append(G_R)
        next_B_candidate.append(G_B)

    if start_with_G[2] != 0:
        B_R = start_with_G[2] + lst[i][0]
        B_G = start_with_G[2] + lst[i][1]
        next_R_candidate.append(B_R)
        next_G_candidate.append(B_G)

    start_with_G[0] = min(next_R_candidate)
    start_with_G[1] = min(next_G_candidate)
    start_with_G[2] = min(next_B_candidate)

# B로 시작한 것
start_with_B = [lst[0][2] + lst[1][0], lst[0][2] + lst[1][1], 0]

for i in range(2, N):
    next_R_candidate = []
    next_G_candidate = []
    next_B_candidate = []

    if start_with_B[0] != 0:
        R_B = start_with_B[0] + lst[i][2]
        R_G = start_with_B[0] + lst[i][1]
        next_B_candidate.append(R_B)
        next_G_candidate.append(R_G)

    if start_with_B[1] != 0:
        G_R = start_with_B[1] + lst[i][0]
        G_B = start_with_B[1] + lst[i][2]
        next_R_candidate.append(G_R)
        next_B_candidate.append(G_B)

    if start_with_B[2] != 0:
        B_R = start_with_B[2] + lst[i][0]
        B_G = start_with_B[2] + lst[i][1]
        next_R_candidate.append(B_R)
        next_G_candidate.append(B_G)

    start_with_B[0] = min(next_R_candidate)
    start_with_B[1] = min(next_G_candidate)
    start_with_B[2] = min(next_B_candidate)

result = []
result.append(start_with_R[1])
result.append(start_with_R[2])
result.append(start_with_G[0])
result.append(start_with_G[2])
result.append(start_with_B[0])
result.append(start_with_B[1])

print(min(result))