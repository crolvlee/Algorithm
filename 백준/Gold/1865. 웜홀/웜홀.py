import sys
input = sys.stdin.readline

# 도로: 양방향
# 웜홀: 단방향

def floyd(distance, N):
    for k in range(1, N + 1):  # 경유지
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    if i == j and distance[i][j] < 0:
                        return "YES"

    return "NO"


TC = int(input())
for _ in range(TC):
    # N: 지점의 수, M: 도로의 수, W: 웜홀의 수
    N, M, W = map(int, input().split())

    distance = [[1e4] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        distance[i][i] = 0

    # 로드, 웜홀 상관 없이 제일 작은 거리 하나 남기기
    # 1. 로드
    for _ in range(M):
        S, E, T = map(int, input().split())
        if distance[S][E] > T:
            distance[S][E] = T
        if distance[E][S] > T:
            distance[E][S] = T

    # 2. 웜홀
    for _ in range(W):
        S, E, T = map(int, input().split())
        if distance[S][E] > -T:
            distance[S][E] = -T

    # 답 찾기
    result = floyd(distance, N)
    print(result)
