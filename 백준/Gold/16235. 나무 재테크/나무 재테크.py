import sys
input = sys.stdin.readline
from collections import deque

# 편의상 행렬의 제일 왼쪽 윗칸을 (0, 0)으로 하겠음

# N: 땅의 가로,세로
# M: 처음 심는 나무의 개수
# K: K년 후 살아있는 나무의 개수를 구할 것임!
N, M, K = map(int, input().split())
yangbun_table = [[5] * N for _ in range(N)]

A = []  # 겨울에 필요
for _ in  range(N):
    line = list(map(int, input().split()))
    A.append(line)

tree_dict = {}

for i in range(N):
    for j in range(N):
        tree_dict[(i, j)] = deque()

for _ in range(M):
    x, y, z = map(int, input().split())
    tree_dict[(x - 1, y - 1)].append(z)

# 초기에 나무의 나이 정렬하기
for tree_pos, age_list in tree_dict.items():
    tree_dict[tree_pos] = deque(sorted(age_list))

# ================================================================

for i in range(K):
    # 봄
    dead_tree_dict = {}
    for tree_pos, age_list in tree_dict.items():
        now_row = tree_pos[0]
        now_col = tree_pos[1]
        new_age_deque = deque()

        while age_list:
            age = age_list.popleft()
            now_yangbun = yangbun_table[now_row][now_col]
            # 나이가 남은 양분보다 적거나 같다면
            if now_yangbun >= age:
                yangbun_table[now_row][now_col] -= age
                new_age = age + 1
                new_age_deque.append(new_age)
            # 나이가 남은 양분보다 많다면
            else:
                if tree_pos in dead_tree_dict:
                    dead_tree_dict[tree_pos].append(age)
                else:
                    dead_tree_dict[tree_pos] = [age]

        tree_dict[tree_pos] = new_age_deque


    # ==================
    # 여름
    for tree_pos, age_list in dead_tree_dict.items():
        now_row = tree_pos[0]
        now_col = tree_pos[1]
        for age in age_list:
            plus_yangbun = age // 2
            yangbun_table[now_row][now_col] += plus_yangbun

    # ==================
    # 가을
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(N):
        for j in range(N):
            for age in tree_dict[(i, j)]:
                if age % 5 == 0:
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < N and 0 <= nj < N:
                            tree_dict[(ni, nj)].appendleft(1)

    # ==================
    # 겨울
    for i in range(N):
        for j in range(N):
            yangbun_table[i][j] += A[i][j]

answer = 0
for tree_pos, age_list in tree_dict.items():
    answer += len(age_list)

print(answer)