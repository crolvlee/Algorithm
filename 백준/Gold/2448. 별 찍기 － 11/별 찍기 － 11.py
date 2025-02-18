def make_basic(table, start_row, start_col):
    table[start_row][start_col] = "*"
    table[start_row + 1][start_col - 1] = "*"
    table[start_row + 1][start_col + 1] = "*"
    table[start_row + 2][start_col - 2] = "*"
    table[start_row + 2][start_col - 1] = "*"
    table[start_row + 2][start_col] = "*"
    table[start_row + 2][start_col + 1] = "*"
    table[start_row + 2][start_col + 2] = "*"


def draw_triangle(table, start_row, start_col, size):
    if size == 3:
        make_basic(table, start_row, start_col)
    else:
        half = size // 2
        draw_triangle(table, start_row, start_col, half)  # 위쪽 삼각형
        draw_triangle(table, start_row + half, start_col - half, half)  # 왼쪽 아래 삼각형
        draw_triangle(table, start_row + half, start_col + half, half)  # 오른쪽 아래 삼각형


N = int(input())
ga = N * 2 - 1
table = [[" "] * ga for _ in range(N)]

draw_triangle(table, 0, ga // 2, N)

# 출력
for line in table:
    print("".join(line))
