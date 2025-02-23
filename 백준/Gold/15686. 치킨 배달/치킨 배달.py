from itertools import combinations

# 0: 빈 칸
# 1: 집
# 2: 치킨집

def distance(first_row, first_col, second_row, second_col):
    se = second_row - first_row
    ga = second_col - first_col
    
    if se < 0:
        se = -se
    if ga < 0:
        ga = -ga
    
    return se + ga

# 입력받기
N, M = map(int, input().split())
ground = []
for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)

# 집의 위치
house_pos = []
for i in range(N):
    for j in range(N):
        if ground[i][j] == 1:
            house_pos.append([i, j])

# 치킨집 M개 선택
chicken_pos = []    # [[행 번호, 열 번호], ]
for i in range(N):
    for j in range(N):
        if ground[i][j] == 2:
            chicken_pos.append([i, j])

selected_chicken_pos = combinations(chicken_pos, M)


# 선택된 조합별 도시의 치킨거리 구하기
dist_list = []

for chicken_combi in selected_chicken_pos:
    dist_cnt = 0

    for h_pos in house_pos:
        h_pos_row = h_pos[0]
        h_pos_col = h_pos[1]
        h_to_c_list = []

        for c_pos in chicken_combi:
            c_pos_row = c_pos[0]
            c_pos_col = c_pos[1]

            dist = distance(h_pos_row, h_pos_col, c_pos_row, c_pos_col)
            h_to_c_list.append(dist)

        h_c_dist = min(h_to_c_list)
        dist_cnt += h_c_dist

    dist_list.append(dist_cnt)

print(min(dist_list))
