# 1~100까지의 칸 있음
# 주사위 -> 주사위 값만큼 위치 값이 커짐 (100번 칸을 넘어가는 건 안됨)
# 사다리 -> 위치 값이 커짐
# 뱀 -> 위치 값이 작아짐

# 너비 우선 탐색 BFS (큐)

from collections import deque

# 입력받기
N, M = map(int, input().split())    # N: 사다리의 개수, M: 뱀의 개수
road_list = []

for _ in range(N):
    x, y = map(int, input().split())
    road_list.append([x, y])

for _ in range(M):
    u, v = map(int, input().split())
    road_list.append([u, v])

# BFS함수 정의
def BFS(start, visited):
    q = deque([[start, 0]])     # [숫자, 지금까지 주사위 굴린 횟수]
    visited[start] = True

    while q:
        now_num, now_cnt = q.popleft()

        if now_num == 100:
            return now_cnt

        # 1. 사다리나 뱀에 해당하는건지 확인
        is_road = False
        for road in road_list:
            if road[0] == now_num:
                next_num = road[1]
                q.appendleft([next_num, now_cnt])
                visited[next_num] = True
                is_road = True
                break
        
        # 2. 사다리나 뱀에 해당하지 않다면, 주사위
        if is_road == False:
            for i in range(1, 7):
                next_num = now_num + i
                next_cnt = now_cnt + 1
                if next_num <= 100 and visited[next_num] == False:
                    q.append([next_num, next_cnt])
                    visited[next_num] = True


# BFS 함수 실행하기!
visited = [False] * 101
answer = BFS(1, visited)
print(answer)