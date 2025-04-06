# 입력받기
N, L = map(int, input().split())
ground = []
road_list = []

for _ in range(N):
    line = list(map(int, input().split()))
    ground.append(line)
    road_list.append(line)

for col in range(0, N):
    now_line = []
    for row in range(0, N):
        now_line.append(ground[row][col])
    road_list.append(now_line)

# ==========================================================
# 경사로를 두는 함수
def build_ramp(road, small_height_idx, big_height_idx):
    small_height = road[small_height_idx]

    # small_height 연속되는게 몇 칸인지 찾기 (경사로가 깔려 있으면 카운트 X)
    small_height_cnt = 0

    if small_height_idx < big_height_idx:
        now_small_height_idx = small_height_idx
        while True:
            if now_small_height_idx >= 0 and road[now_small_height_idx] == small_height and ramp[now_small_height_idx] == False:
                small_height_cnt += 1
                now_small_height_idx -= 1
            else:
                break
    elif small_height_idx > big_height_idx:
        now_small_height_idx = small_height_idx
        while True:
            if now_small_height_idx <= N-1 and road[now_small_height_idx] == small_height:
                small_height_cnt += 1
                now_small_height_idx += 1
            else:
                break

    # ============================================
    # 연속되는 small_height의 수가 L보다 작다면 -> 안됨
    if small_height_cnt < L:
        return False

    # 연속되는 small_height의 수가 L보다 크거나 같다면  -> 됨
    else:
        # 경사로 반영
        if small_height_idx < big_height_idx:
            now_cnt = 0
            while now_cnt != L:
                ramp[small_height_idx] = True
                small_height_idx -= 1
                now_cnt += 1
        elif small_height_idx > big_height_idx:
            now_cnt = 0
            while now_cnt != L:
                ramp[small_height_idx] = True
                small_height_idx += 1
                now_cnt += 1

    return True

# ====================
answer = 0

for road in road_list:
    ok = True
    ramp = [False] * N      # 경사로가 이미 깔려 있는 칸에는 경사로를 떠 놓지 못함

    for i in range(0, N-1):
        if abs(road[i] - road[i+1]) >= 2:
            ok = False
            break

        elif abs(road[i] - road[i + 1]) == 0:
            continue

        elif abs(road[i] - road[i+1]) == 1:
            result = True
            if road[i] < road[i+1]:
                small_height_idx = i
                big_height_idx = i + 1
                result = build_ramp(road, small_height_idx, big_height_idx)

            elif road[i] > road[i+1]:
                small_height_idx = i+1
                big_height_idx = i
                result = build_ramp(road, small_height_idx, big_height_idx)

            if result == False:
                ok = False
                break

    if ok == True:
        answer += 1




print(answer)