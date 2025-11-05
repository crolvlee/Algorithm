
# 입력받기
N, M = map(int, input().split())
ground = []
for _ in range(N):
    line = input()
    ground.append(line)

# 그룹 묶기
# -1: 아직 방문하지 않은 그룹
group = [[-1] * M for _ in range(N)]
answer = 0

def DFS(now_row, now_col, lst):
    global answer
    if group[now_row][now_col] == -1:
        if len(lst) == 0:
            answer += 1
        group[now_row][now_col] = answer
        new_lst = lst[:] + [[now_row, now_col]]

        if ground[now_row][now_col] == 'U':
            DFS(now_row - 1, now_col, new_lst)
        elif ground[now_row][now_col] == 'D':
            DFS(now_row + 1, now_col, new_lst)
        elif ground[now_row][now_col] == 'L':
            DFS(now_row, now_col - 1, new_lst)
        elif ground[now_row][now_col] == 'R':
            DFS(now_row, now_col + 1, new_lst)

    elif group[now_row][now_col] == answer:
        return
    
    else:
        now_group_num = group[now_row][now_col]
        group[now_row][now_col] = now_group_num
        for point in lst:
            r, c = point[0], point[1]
            group[r][c] = now_group_num
        answer -= 1
        return


# 하나씩 돌기
for i in range(N):
    for j in range(M):
        # 현재 시작점은 i행 j열
        if group[i][j] == -1:
            a = DFS(i, j, [])

print(answer)