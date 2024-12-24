# 입력 받기
n = int(input())     # 지도의 크기
ground = []

for _ in range(n):
    line = []
    line_input = input()
    for li in line_input:
        line.append(int(li))
    ground.append(line)
    

# DFS함수 정의 -> 이미 탐색한 곳은 2로 바꾸기
def DFS(ground, row, col):
    ground[row][col] = 2
    current_sum = 1

    # 주변 탐색
    if col+1 < n and ground[row][col+1] == 1:     # 오른쪽
        current_sum += DFS(ground, row, col+1)
    if row+1 < n and ground[row+1][col] == 1:     # 아랫쪽
        current_sum += DFS(ground, row+1, col)
    if col-1 >= 0 and ground[row][col-1] == 1:     # 왼쪽
        current_sum += DFS(ground, row, col-1)
    if row-1 >= 0 and ground[row-1][col] == 1:     # 윗쪽
        current_sum += DFS(ground, row-1, col)

    return current_sum

# 단지별 집의 수 카운트
# len(groups)가 단지 수
groups = []

# ground 탐색
for r in range(n):
    for c in range(n):
        if ground[r][c] == 1:
            current_sum = DFS(ground, r, c)
            groups.append(current_sum)
        
print(len(groups))
groups.sort()
for g in groups:
    print(g)