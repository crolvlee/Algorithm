# 편의상 제일 왼쪽 윗 칸을 (0, 0)으로 하겠음

# 방향 정의
directions_dict = {0: (0, 1), 1: (-1, 0), 2: (0, -1), 3: (1, 0)}

# N: 드래곤 커브의 수
N = int(input())
ground = [[0] * 101 for _ in range(101)]

for _ in range(N):
    # x: 열 번호 / y: 행 변호 / d: 시작 방향 / g: 세대
    x, y, d, g = map(int, input().split())
    direction_store = [d]

    for i in range(1, g+1):     # i는 현재 세대
        new_direction_list = []
        for direction in direction_store[::-1]:
            if direction == 0:
                new_direction_list.append(1)
            elif direction == 1:
                new_direction_list.append(2)
            elif direction == 2:
                new_direction_list.append(3)
            elif direction == 3:
                new_direction_list.append(0)

        direction_store += new_direction_list


    # 시작점에서 방향 따라서 가기
    now_row = y
    now_col = x
    ground[now_row][now_col] = 1
    for direction in direction_store:
        d_row, d_col = directions_dict[direction]
        ground[now_row + d_row][now_col + d_col] = 1    # 격자 밖을 벗어나지 않으니 검증 필요X
        now_row += d_row
        now_col += d_col


answer = 0
for i in range(0, 100):
    for j in range(0, 100):
        if ground[i][j] == 1 and ground[i+1][j] == 1 and ground[i][j+1] == 1 and ground[i+1][j+1] == 1:
            answer += 1

print(answer)

