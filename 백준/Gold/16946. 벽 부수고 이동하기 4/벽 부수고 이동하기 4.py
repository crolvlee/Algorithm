from collections import deque

# 1. 입력받기
N, M = map(int, input().split())
ground = []

for _ in range(N):
    line = list(map(int, input()))
    ground.append(line)


# 2. 0끼리의 그룹 번호를 ground에 넣기 / 그룹번호는 2번부터 시작
group_cnt = {}
group_num = 2
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # 동서남북

for i in range(N):
    for j in range(M):
        if ground[i][j] == 0:
            # BFS 함수 정의
            def BFS(start_row, start_col):
                q = deque()
                q.append([start_row, start_col])

                while q:
                    now_row, now_col = q.popleft()

                    for d_row, d_col in directions:
                        next_row = now_row + d_row
                        next_col = now_col + d_col
                        if 0 <= next_row <= N-1 and 0 <= next_col <= M-1 and ground[next_row][next_col] == 0:
                            group_cnt[group_num] += 1
                            ground[next_row][next_col] = group_num
                            q.append([next_row, next_col])

            group_cnt[group_num] = 1
            ground[i][j] = group_num
            BFS(i, j)
            group_num += 1


# 3. 1인 것의 동서남북 이어진 0 찾기
result = []

for i in range(N):
    res_line = []
    for j in range(M):
        if ground[i][j] == 1:
            # 동서남북에 있는 그룹 번호 찾기
            group_num_set = set()
            for d_row, d_col in directions:
                next_row = i + d_row
                next_col = j + d_col
                if 0 <= next_row <= N-1 and 0 <= next_col <= M-1 and ground[next_row][next_col] != 1:
                    group_num_set.add(ground[next_row][next_col])
            
            now_res = 1
            for group_num in group_num_set:
                now_res += group_cnt[group_num]
            
            res_line.append(now_res)
        else:
            res_line.append(0)
    
    result.append(res_line)


for line in result:
    line_str = ''
    for k in range(M):
        line_str += str(line[k] % 10)
    print(line_str)
