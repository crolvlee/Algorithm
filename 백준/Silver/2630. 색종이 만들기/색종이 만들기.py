# 1: blue
# 0: white

# 입력받기
N = int(input())
table = []
for _ in range(N):
    line = list(map(int, input().split()))
    table.append(line)

# 색종이 개수 카운트
blue_cnt = 0
white_cnt = 0

# 재귀함수
def recursion(start_row, start_col, N):
    
    global blue_cnt
    global white_cnt
    part_cnt = int((N * N) / 4)

    # -------------------
    # 1사분면
    list_1 = []
    for i in range(start_row, start_row + (N // 2)):
        for j in range(start_col + (N // 2), start_col + (N // 2) + (N // 2)):
            list_1.append(table[i][j])

    # full인지 확인
    if list_1.count(1) == part_cnt:
        blue_cnt += 1
    elif list_1.count(0) == part_cnt:
        white_cnt += 1
    else:
        recursion(start_row, start_col + (N // 2), N // 2)

    # -------------------
    # 2사분면
    list_2 = []
    for i in range(start_row, start_row + (N // 2)):
        for j in range(start_col, start_col + (N // 2)):
            list_2.append(table[i][j])

    # full인지 확인
    if list_2.count(1) == part_cnt:
        blue_cnt += 1
    elif list_2.count(0) == part_cnt:
        white_cnt += 1
    else:
        recursion(start_row, start_col, N // 2)

    # -------------------
    # 3사분면
    list_3 = []
    for i in range(start_row + N // 2, start_row + (N // 2) + (N // 2)):
        for j in range(start_col, start_col + (N // 2)):
            list_3.append(table[i][j])

    # full인지 확인
    if list_3.count(1) == part_cnt:
        blue_cnt += 1
    elif list_3.count(0) == part_cnt:
        white_cnt += 1
    else:
        recursion(start_row + (N // 2), start_col, N // 2)

    # -------------------
    # 4사분면
    list_4 = []
    for i in range(start_row + (N // 2), start_row + (N // 2) + (N // 2)):
        for j in range(start_col + (N // 2), start_col + (N // 2) + (N // 2)):
            list_4.append(table[i][j])

    # full인지 확인
    if list_4.count(1) == part_cnt:
        blue_cnt += 1
    elif list_4.count(0) == part_cnt:
        white_cnt += 1
    else:
        recursion(start_row + (N // 2), start_col + (N // 2), N // 2)


list_first = []
for i in range(0, N):
    for j in range(0, N):
        list_first.append(table[i][j])

if list_first.count(1) == (N * N):
    blue_cnt += 1
elif list_first.count(0) == (N * N):
    white_cnt += 1
else:
    recursion(0, 0, N)

print(white_cnt)
print(blue_cnt)
