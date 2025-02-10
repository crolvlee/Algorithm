def count_change(now_board):
    w_board_cnt = 0
    b_board_cnt = 0

    line_w = ["W", "B", "W", "B", "W", "B", "W", "B"]
    line_b = ["B", "W", "B", "W", "B", "W", "B", "W"]

    # 1. 만들 체스판의 시작이 W인 경우
    for row_idx, line in enumerate(now_board):
        # W로 시작하는 줄일 경우
        if row_idx % 2 == 0:
            for col_idx in range(0, 8):
                if line[col_idx] != line_w[col_idx]:
                    w_board_cnt += 1

        # B로 시작하는 줄일 경우
        else:
            for col_idx in range(0, 8):
                if line[col_idx] != line_b[col_idx]:
                    w_board_cnt += 1

    # 2. 만들 체스판의 시작이 B인 경우
    for row_idx, line in enumerate(now_board):
        # W로 시작하는 줄일 경우
        if row_idx % 2 == 1:
            for col_idx in range(0, 8):
                if line[col_idx] != line_w[col_idx]:
                    b_board_cnt += 1

        # B로 시작하는 줄일 경우
        else:
            for col_idx in range(0, 8):
                if line[col_idx] != line_b[col_idx]:
                    b_board_cnt += 1

    return min(w_board_cnt, b_board_cnt)

M, N = map(int, input().split())
board = []
cnt_list = []

for _ in range(M):
    line = list(map(str, input().strip()))
    board.append(line)

# 시작점에 따라서 필요한 색칠 개수 구하기
for i in range(0, M-7):
    for j in range(0, N-7):
        # 시작점이 i행 j열일 때의 8x8 보드
        now_board = []
        for a in range(i, i+8):
            line = []
            for b in range(j, j+8):
                line.append(board[a][b])
            now_board.append(line)
        
        # 현재 보드에서 바꿔야하는 색칠 개수 구하기
        cnt = count_change(now_board)
        cnt_list.append(cnt)

print(min(cnt_list))