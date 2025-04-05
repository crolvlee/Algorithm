# 뽑는 개수는 N
def DFS(depth, now_row, now_col, cost):
    global min_cost
    if depth == N:
        final_cost = cost + abs(now_row - house_row) + abs(now_col - house_col)
        if final_cost < min_cost:
            min_cost = final_cost
        return

    for i in range(N):
        if visited[i] == False:
            next_row = customer[i][0]
            next_col = customer[i][1]
            next_cost = abs(next_row - now_row) + abs(next_col - now_col)
            visited[i] = True

            DFS(depth + 1, next_row, next_col, cost + next_cost)

            visited[i] = False


T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())

    # 회사의 좌표, 집의 좌표, 고객의 좌표
    line = list(map(int, input().split()))

    company_row = line[0]
    company_col = line[1]
    house_row = line[2]
    house_col = line[3]

    rest = line[4:]
    customer = []

    for i in range(0, N*2, 2):
        c_row = rest[i]
        c_col = rest[i+1]
        customer.append((c_row, c_col))

    visited = [False] * N
    min_cost = 1e9

    DFS(0, company_row, company_col, 0)

    answer = min_cost
    print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
