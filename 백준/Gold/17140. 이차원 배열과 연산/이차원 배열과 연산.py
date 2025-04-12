# 편의상 제일 왼쪽 위가 (0, 0)

r, c, k = map(int, input().split())
r = r-1
c = c-1

A = []
for _ in range(3):
    line = list(map(int, input().split()))
    A.append(line)

# =====================================
def arr_sort(arr):
    num_dict = {}
    for num in arr:
        if num == 0:
            continue
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1

    num_lst = []
    for num, cnt in num_dict.items():
        num_lst.append([cnt, num])

    num_lst.sort()

    result = []
    for lst in num_lst:
        result.append(lst[1])
        result.append(lst[0])

    return result

# =====================================

if r < 3 and c < 3 and A[r][c] == k:
    print(0)
else:
    # A 배열의 전체 크기를 저장
    A_row = 3
    A_col = 3

    now_time = 0
    found = False

    while True:
        if now_time == 101:
            break

        now_time += 1

        # 1. R 연산 수행
        if A_row >= A_col:
            # new_A에 연산결과 넣기
            new_A = []
            for i in range(A_row):
                after_row = arr_sort(A[i])
                if len(after_row) > 100:
                    new_A.append(after_row[:100])
                else:
                    new_A.append(after_row)

            if len(new_A) > 100:
                new_A = new_A[:100]

            # new_A에 0채워 넣을 것 있으면 채우기
            max_new_A_col = 0
            for line in new_A:
                if len(line) > max_new_A_col:
                    max_new_A_col = len(line)

            for idx, line in enumerate(new_A):
                if len(line) < max_new_A_col:
                    zero_list = [0] * (max_new_A_col - len(line))
                    new_A[idx] = line[:] + zero_list[:]

            # A를 new_A로 교체
            A = new_A[:]
            A_row = len(A)
            A_col = len(A[0])

        # 2. C 연산 수행
        else:
            # new_A_reverse에 연산결과 넣기
            new_A_reverse = []      # 주의! 이 행렬의 0행에 있는건 사실상 0열에 있는것!

            for i in range(A_col):
                now_col = []
                for j in range(A_row):
                    now_col.append(A[j][i])

                after_col = arr_sort(now_col)
                if len(after_col) > 100:
                    new_A_reverse.append(after_col[:100])
                else:
                    new_A_reverse.append(after_col)

            if len(new_A_reverse) > 100:
                new_A_reverse = new_A_reverse[:100]

            # new_A_reverse에 0 채워넣을 것 있으면 채우기
            max_new_A_row = 0
            for line in new_A_reverse:
                if len(line) > max_new_A_row:
                    max_new_A_row = len(line)

            for idx, line in enumerate(new_A_reverse):
                if len(line) < max_new_A_row:
                    zero_list = [0] * (max_new_A_row - len(line))
                    new_A_reverse[idx] = line[:] + zero_list[:]

            # A를 new_A_reverse 행렬 바꾼걸로 교체
            reverse_row = len(new_A_reverse)
            reverse_col = len(new_A_reverse[0])
            A = [[0] * reverse_row for _ in range(reverse_col)]
            A_row = reverse_col
            A_col = reverse_row

            for i in range(reverse_col):
                for j in range(reverse_row):
                    A[i][j] = new_A_reverse[j][i]

        # 연산 끝난 후, 결과 확인
        if r < A_row and c < A_col:
            if A[r][c] == k:
                found = True
                break
        else:
            continue


    if found == True:
        print(now_time)
    else:
        print(-1)