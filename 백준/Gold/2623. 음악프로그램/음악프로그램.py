from collections import deque

# 1. 입력받기
N, M = map(int, input().split())    # N: 가수의 수 / M: PD의 수
in_node_cnt = {}                    # in_node_dict = {1: 0, 2: 1, 3: 2, ...}
in_nodes = {}
out_nodes = {}                      # out_nodes = {1: [4], 2: [3, 5], ...}

for i in range(1, N+1):
    in_node_cnt[i] = 0
    in_nodes[i] = set()
    out_nodes[i] = set()

for _ in range(M):
    lst = list(map(int, input().split()))
    lst = lst[1:]
    for i in range(0, len(lst) - 1):
        start_node = lst[i]
        end_node = lst[i+1]
        out_nodes[start_node].add(end_node)
        in_nodes[end_node].add(start_node)

for i in range(1, N+1):
    in_node_cnt[i] = len(in_nodes[i])

# 2. 위상정렬
result = []
q = deque()
visited = [False] * (N+1)

while True:
    if len(result) == N:
        break

    # 2-1. 큐에 넣기
    for k in in_node_cnt:
        v = in_node_cnt[k]
        if v == 0:
            if visited[k] == False:
                q.append(k)
                visited[k] = True

    # 2-2. 큐에 있는 노드 중 제일 앞 노드를 선택
    if len(q) > 0:
        now_node = q.popleft()
        result.append(now_node)
        next_nodes = out_nodes[now_node]
        for next_node in next_nodes:
            if visited[next_node] == False:
                in_node_cnt[next_node] -= 1
    else:
        break


# 3. 출력
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)
