N, M = map(int, input().split())    # 듣, 보

# 듣
person_list = []
for _ in range(N):
    person = input()
    person_list.append(person)
    
person_list = set(person_list)
# set에서 in 연산자 -> O(1)

# 보
result_list = []
for _ in range(M):
    person = input()
    if person in person_list:
        result_list.append(person)

print(len(result_list))

result_list.sort()
for r in result_list:
    print(r)