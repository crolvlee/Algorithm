from collections import deque

def BFS():
    q = deque()

    # 방문 상태를 문자열로 저장
    visited = set()
    
    # 시작 상태 설정
    start_char = ground[0][0]
    start_visited = start_char
    q.append((0, 0, start_visited, 1))
    visited.add((0, 0, start_visited))

    max_depth = 0

    while q:
        row, col, now_visited, depth = q.popleft()
        max_depth = max(max_depth, depth)

        # 상
        if row - 1 >= 0:
            next_char = ground[row - 1][col]
            if next_char not in now_visited:
                next_visited = now_visited + next_char
                if (row - 1, col, next_visited) not in visited:
                    visited.add((row - 1, col, next_visited))
                    q.append((row - 1, col, next_visited, depth + 1))

        # 하
        if row + 1 < R:
            next_char = ground[row + 1][col]
            if next_char not in now_visited:
                next_visited = now_visited + next_char
                if (row + 1, col, next_visited) not in visited:
                    visited.add((row + 1, col, next_visited))
                    q.append((row + 1, col, next_visited, depth + 1))

        # 좌
        if col - 1 >= 0:
            next_char = ground[row][col - 1]
            if next_char not in now_visited:
                next_visited = now_visited + next_char
                if (row, col - 1, next_visited) not in visited:
                    visited.add((row, col - 1, next_visited))
                    q.append((row, col - 1, next_visited, depth + 1))

        # 우
        if col + 1 < C:
            next_char = ground[row][col + 1]
            if next_char not in now_visited:
                next_visited = now_visited + next_char
                if (row, col + 1, next_visited) not in visited:
                    visited.add((row, col + 1, next_visited))
                    q.append((row, col + 1, next_visited, depth + 1))

    return max_depth


# 입력 받기
R, C = map(int, input().split())
ground = [input().strip() for _ in range(R)]

# BFS 실행
answer = BFS()
print(answer)
