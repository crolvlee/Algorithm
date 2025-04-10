from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # 상하좌우
N = int(input())
ground = []

sang_row = 0
sang_col = 0

for i in range(N):
    line = list(map(int, input().split()))
    if 9 in line:
        sang_row = i
        sang_col = line.index(9)
    ground.append(line)

ground[sang_row][sang_col] = 0      # ground에는 물고기만 담는 방식

# ========================================
# 현재 상어가 자신의 크기보다 작은 물고기 위치로 갈 수 있는지 확인
# 이동한 거리, 도착점 row, 도착점 col을 리턴
def BFS(sang_row, sang_col, sang_size):
    visited = [[False] * N for _ in range(N)]
    visited[sang_row][sang_col] = True

    q = deque()
    q.append([sang_row, sang_col, 0])

    final_depth = 0
    final_pos = []
    found = False

    while q:
        now_row, now_col, now_depth = q.popleft()

        if found == True and now_depth > final_depth:
            break

        if ground[now_row][now_col] != 0 and ground[now_row][now_col] < sang_size:
            if found == False:
                final_depth = now_depth
                found = True

            final_pos.append((now_row, now_col))
            continue


        if len(final_pos) > 0:
            if ground[now_row][now_col] != 0 and ground[now_row][now_col] < sang_size:
                final_pos.append((now_row, now_col))
                continue
            else:
                continue


        for direction in directions:
            d_row = direction[0]
            d_col = direction[1]
            if 0 <= now_row + d_row and now_row + d_row <= N-1 and 0 <= now_col + d_col and now_col + d_col <= N-1:
                if visited[now_row + d_row][now_col + d_col] == False:
                    # 현재 상어 사이즈와 비교 -> 작거나 같으면 이동!!!
                    # 빈칸이어도 이동 가능
                    if ground[now_row + d_row][now_col + d_col] <= sang_size:
                        q.append([now_row + d_row, now_col + d_col, now_depth + 1])
                        visited[now_row + d_row][now_col + d_col] = True

    # final_pos 중에 행렬 우선인 것 찾기
    final_pos.sort()

    if len(final_pos) == 0:
        final_row = -1
        final_col = -1
        # 이건 주의! 뒤에서 이거 사용하면 안됨

    else:
        final_pos.sort()
        final_row = final_pos[0][0]
        final_col = final_pos[0][1]

    return final_depth, final_row, final_col



# ========================================
now_sang_row = sang_row
now_sang_col = sang_col
now_sang_size = 2
now_sang_fish_sum = 0     # 현재 상어 뱃속에 있는 물고기 카운트 (상어 크기가 커지면 이건 비워짐)

answer = 0  # 총 이동 거리

while True:
    # 이동할 거리, 이동할 행, 이동할 열
    dist, arrive_row, arrive_col = BFS(now_sang_row, now_sang_col, now_sang_size)

    # 더 이상 못 먹으면 break
    if dist == 0:
        break


    now_sang_fish_sum += 1
    ground[arrive_row][arrive_col] = 0
    now_sang_row = arrive_row
    now_sang_col = arrive_col


    answer += dist

    # 상어가 사이즈업 할 수 있는지 확인
    if now_sang_fish_sum == now_sang_size:
        now_sang_size += 1
        now_sang_fish_sum = 0

print(answer)

