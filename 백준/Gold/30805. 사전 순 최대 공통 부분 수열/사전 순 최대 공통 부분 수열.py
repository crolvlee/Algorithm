N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
B_list = list(map(int, input().split()))

# 결과 찾기
result = []
A_idx = 0
B_idx = 0

while True:
    if A_idx >= N or B_idx >= M:
        break

    A_next_set = set(A_list[A_idx:])
    B_next_set = set(B_list[B_idx:])
    common_set = A_next_set.intersection(B_next_set)


    if len(common_set) != 0:
        max_num = max(common_set)
        result.append(str(max_num))

        A_idx = A_list[A_idx:].index(max_num) + A_idx + 1
        B_idx = B_list[B_idx:].index(max_num) + B_idx + 1

    else:
        break

print(len(result))
print(" ".join(result))
