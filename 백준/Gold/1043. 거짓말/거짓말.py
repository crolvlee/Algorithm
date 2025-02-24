# N: 사람의 수, M: 파티의 수
N, M = map(int, input().split())
second = list(map(int, input().split()))

know_count = second[0]
know_people = []  # 사람들의 번호는 1부터 N까지!
if know_count >= 1:
    know_people = second[1:]

party_list = []
for i in range(M):
    line = list(map(int, input().split()))
    party_list.append(line[1:])

# 그래프 만들기 (for 각 점이 연결된 점이 뭔지 확인)
graph = [[] for _ in range(N+1)]

for party in party_list:
    for i, person_id in enumerate(party):
        for j in range(i+1, len(party)):
            neighbor_id = party[j]
            graph[person_id].append(neighbor_id)
            graph[neighbor_id].append(person_id)

# DFS 함수 정의
def DFS(person_id, graph):
    global new_know_people
    
    new_know_people[person_id] = True
    
    for neighbor_id in graph[person_id]:
        if new_know_people[neighbor_id] == False:
            DFS(neighbor_id, graph)

# DFS 함수 실행하면서 know_people가 연결된 것들 찾기
new_know_people = [False] * (N+1)   

for person_id in know_people:
    DFS(person_id, graph)


# 각 파티에서 거짓말이 가능한지 확인
answer = 0
for party in party_list:
    canLie = True
    for person_id in party:
        if new_know_people[person_id] == True:
            canLie = False
            break

    if canLie == True:
        answer += 1

print(answer)