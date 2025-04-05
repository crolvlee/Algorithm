T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    t_c = int(input())
    ground = []
    for _ in range(100):
        line = list(map(int, input().split()))
        ground.append(line)

    now_row = 99
    now_col = ground[-1].index(2)

    visited = [[False] * 100 for _ in range(100)]

    while True:
        visited[now_row][now_col] = True

        if now_row == 0:
            break

        if now_row == 99:
            now_row -= 1
            continue

        # 좌, 우 확인
        if now_col - 1 >= 0 and ground[now_row][now_col - 1] == 1:
            if visited[now_row][now_col - 1] == False:
                now_col -= 1
                continue
        if now_col + 1 <= 99 and ground[now_row][now_col + 1] == 1:
            if visited[now_row][now_col + 1] == False:
                now_col += 1
                continue

        # 좌, 우에 길 없는 경우 -> 위로 올라가기
        now_row -= 1


    answer = now_col
    print(f"#{t_c} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
