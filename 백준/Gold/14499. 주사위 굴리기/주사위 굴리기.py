# 입력받기
# N: 세로 크기, M: 가로 크기
N, M, x, y, K = map(int, input().split())

dice_row = x
dice_col = y

ground = []

for _ in range(0, N):
    line = list(map(int, input().split()))
    ground.append(line)

command_list = list(map(int, input().split()))

# ==========================================
# 주사위 각 자리에 있는 것
# dice[0]: 천장에 있는 숫자
# dice[5]: 바닥에 있는 숫자
dice = [0, 0, 0, 0, 0, 0]

# 주사위 회전시키는 함수
def rotate_dice(direction):
    global dice
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

    # 동쪽 방향
    if direction == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    # 서쪽 방향
    elif direction == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    # 북쪽 방향
    elif direction == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

    # 남쪽 방향
    elif direction == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

# ==========================================

for command in command_list:

    # 동
    if command == 1:
        if dice_col + 1 <= M-1:
            dice_col += 1
            rotate_dice(1)

            print(dice[0])

            # 1. 이동 후 ground 칸에 적힌 수가 0인 경우
            if ground[dice_row][dice_col] == 0:
                ground[dice_row][dice_col] = dice[5]

            # 2. 이동 후 ground 칸에 적힌 수가 0이 아닌 경우
            else:
                dice[5] = ground[dice_row][dice_col]
                ground[dice_row][dice_col] = 0

    # 서
    elif command == 2:
        if dice_col - 1 >= 0:
            dice_col -= 1
            rotate_dice(2)

            print(dice[0])

            # 1. 이동 후 ground 칸에 적힌 수가 0인 경우
            if ground[dice_row][dice_col] == 0:
                ground[dice_row][dice_col] = dice[5]

            # 2. 이동 후 ground 칸에 적힌 수가 0이 아닌 경우
            else:
                dice[5] = ground[dice_row][dice_col]
                ground[dice_row][dice_col] = 0



    # 북
    elif command == 3:
        if dice_row - 1 >= 0:
            dice_row -= 1
            rotate_dice(3)

            print(dice[0])

            # 1. 이동 후 ground 칸에 적힌 수가 0인 경우
            if ground[dice_row][dice_col] == 0:
                ground[dice_row][dice_col] = dice[5]

            # 2. 이동 후 ground 칸에 적힌 수가 0이 아닌 경우
            else:
                dice[5] = ground[dice_row][dice_col]
                ground[dice_row][dice_col] = 0


    # 남
    elif command == 4:
        if dice_row + 1 <= N-1:
            dice_row += 1
            rotate_dice(4)

            print(dice[0])

            # 1. 이동 후 ground 칸에 적힌 수가 0인 경우
            if ground[dice_row][dice_col] == 0:
                ground[dice_row][dice_col] = dice[5]

            # 2. 이동 후 ground 칸에 적힌 수가 0이 아닌 경우
            else:
                dice[5] = ground[dice_row][dice_col]
                ground[dice_row][dice_col] = 0





