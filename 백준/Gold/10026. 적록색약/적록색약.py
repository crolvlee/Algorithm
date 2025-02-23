import sys
sys.setrecursionlimit(10000)

# 깊이우선 DFS 함수 정의
def DFS(image, row, col, visited):
    now_color = image[row][col]

    # 상
    if row - 1 >= 0 and visited[row - 1][col] == False:
        if image[row - 1][col] == now_color:
            visited[row - 1][col] = True
            DFS(image, row - 1, col, visited)

    # 하
    if row + 1 <= N - 1 and visited[row + 1][col] == False:
        if image[row + 1][col] == now_color:
            visited[row + 1][col] = True
            DFS(image, row + 1, col, visited)

    # 좌
    if col - 1 >= 0 and visited[row][col - 1] == False:
        if image[row][col - 1] == now_color:
            visited[row][col - 1] = True
            DFS(image, row, col - 1, visited)

    # 우
    if col + 1 <= N - 1 and visited[row][col + 1] == False:
        if image[row][col + 1] == now_color:
            visited[row][col + 1] = True
            DFS(image, row, col + 1, visited)


# ===========
N = int(input())

# 일반 이미지
image_basic = []
for _ in range(N):
    line = input()
    image_basic.append(line)

# 적록색약 이미지
image_blind = []
for line in image_basic:
    new_line = line.replace('G', 'R')
    image_blind.append(new_line)

# 일반 이미지 DFS 실행
visited_basic = [[False] * N for _ in range(N)]
zone_count_basic = 0

for i in range(N):
    for j in range(N):
        if visited_basic[i][j] == False:
            DFS(image_basic, i, j, visited_basic)
            zone_count_basic += 1

# 적록색약 이미지 DFS 실행
visited_blind = [[0] * N for _ in range(N)]
zone_count_blind = 0
for i in range(N):
    for j in range(N):
        if visited_blind[i][j] == False:
            DFS(image_blind, i, j, visited_blind)
            zone_count_blind += 1

print(zone_count_basic, zone_count_blind)
