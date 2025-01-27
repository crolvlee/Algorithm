from collections import deque

def BFS(box_list, tomato_1_pos_list, tomato_0_first):
    tomato_1_pos_list.append([-1, -1, -1])
    q = deque(tomato_1_pos_list)
    days = 0
    tomato_0_cnt = 0
    
    while q:
        tomato_1_pos = q.popleft()
        tomato_1_i = tomato_1_pos[0]    # 높이
        tomato_1_j = tomato_1_pos[1]    # 세로
        tomato_1_k = tomato_1_pos[2]    # 가로

        if tomato_1_i == -1 and tomato_1_j == -1 and tomato_1_k == -1:
            if q:
                days += 1
                q.append([-1, -1, -1])
            continue

        # 위
        if tomato_1_i + 1 <= H-1:
            if box_list[tomato_1_i + 1][tomato_1_j][tomato_1_k] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i + 1][tomato_1_j][tomato_1_k] = 1
                q.append([tomato_1_i + 1, tomato_1_j, tomato_1_k])

        # 아래
        if tomato_1_i - 1 >= 0:
            if box_list[tomato_1_i - 1][tomato_1_j][tomato_1_k] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i - 1][tomato_1_j][tomato_1_k] = 1
                q.append([tomato_1_i - 1, tomato_1_j, tomato_1_k])

        # 왼쪽
        if tomato_1_k - 1 >= 0:
            if box_list[tomato_1_i][tomato_1_j][tomato_1_k - 1] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i][tomato_1_j][tomato_1_k - 1] = 1
                q.append([tomato_1_i, tomato_1_j, tomato_1_k - 1])

        # 오른쪽
        if tomato_1_k + 1 <= M-1:
            if box_list[tomato_1_i][tomato_1_j][tomato_1_k + 1] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i][tomato_1_j][tomato_1_k + 1] = 1
                q.append([tomato_1_i, tomato_1_j, tomato_1_k + 1])

        # 앞
        if tomato_1_j - 1 >= 0:
            if box_list[tomato_1_i][tomato_1_j - 1][tomato_1_k] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i][tomato_1_j - 1][tomato_1_k] = 1
                q.append([tomato_1_i, tomato_1_j - 1, tomato_1_k])

        # 뒤
        if tomato_1_j + 1 <= N-1:
            if box_list[tomato_1_i][tomato_1_j + 1][tomato_1_k] == 0:
                tomato_0_cnt += 1
                box_list[tomato_1_i][tomato_1_j + 1][tomato_1_k] = 1
                q.append([tomato_1_i, tomato_1_j + 1, tomato_1_k])

    if tomato_0_cnt < tomato_0_first:
        return -1

    return days

# ============
# 입력받기
global M, N, H
M, N, H = map(int, input().split())
box_list = []
tomato_0_first = 0    # 제일 처음 주어지는 익지 않은 토마토 개수

for _ in range(H):
    one_box = []
    for _ in range(N):
        line = list(map(int, input().split()))
        one_box.append(line)
        tomato_0_first += line.count(0)

    box_list.append(one_box)


if tomato_0_first == 0:
    print(0)
    
else:
    # 익은 토마토의 위치를 찾기 (처음 큐에 넣을 목적임)
    tomato_1_pos_list = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if box_list[i][j][k] == 1:
                    tomato_1_pos_list.append([i, j, k])



    answer = BFS(box_list, tomato_1_pos_list, tomato_0_first)
    print(answer)
