import heapq

start_num_set_all = set()
end_num_set_all = set()
start_num_dict = {}  # key 뒤에 value가 나와야 함
end_num_dict = {} # key 앞에 value가 나와야 함

# 입력 받기
N, M = map(int, input().split())
for _ in range(M):
    start_num, end_num = map(int, input().split())
    start_num_set_all.add(start_num)
    end_num_set_all.add(end_num)

    if start_num not in start_num_dict:
        start_num_dict[start_num] = [end_num]
    else:
        start_num_dict[start_num].append(end_num)

    if end_num not in end_num_dict:
        end_num_dict[end_num] = [start_num]
    else:
        end_num_dict[end_num].append(start_num)


# -----------------
start_num_lst = []  # start 넣을 수 있는 것
start_num_candidate_lst = [] # start 후보
end_num_lst = []  # end 넣을 수 있는 것
basic_num_lst = [] # 고정 숫자 아닌 것

for s_num in start_num_set_all:
    if s_num not in end_num_set_all:
        heapq.heappush(start_num_lst, s_num)
    else:
        heapq.heappush(start_num_candidate_lst, s_num)

for i in range(1, N+1):
    if i not in start_num_set_all and i not in end_num_set_all:
        heapq.heappush(basic_num_lst, i)

# -----------------
# print(start_num_set_all)
# print(end_num_set_all)
# print(basic_num_lst)

# 앞에서부터 차례대로 넣기
result = []

for i in range(N):

    # 넣을 수 있는 수 찾기
    candidate_lst = []
    min_start_num = 1e9
    min_end_num = 1e9
    min_basic_num = 1e9
    if start_num_lst:
        min_start_num = start_num_lst[0]
        if min_start_num not in result:
            candidate_lst.append(min_start_num)
    if end_num_lst:
        min_end_num = end_num_lst[0]
        if min_end_num not in result:
            candidate_lst.append(min_end_num)
    if basic_num_lst:
        min_basic_num = basic_num_lst[0]
        if min_basic_num not in result:
            candidate_lst.append(min_basic_num)

    min_num = min(candidate_lst)

    # 1. start_num_lst에 있는 것 넣기
    if min_num == min_start_num:
        result.append(min_start_num)
        heapq.heappop(start_num_lst)

        # 현재 수(min_start_num) 뒤에 올 수 있는 것 정리
        for a in start_num_dict[min_start_num]:
            if len(end_num_dict[a]) > 0:
                end_num_dict[a].remove(min_start_num)
            if len(end_num_dict[a]) == 0:
                if a in start_num_candidate_lst:
                    heapq.heappush(start_num_lst, a)
                else:
                    heapq.heappush(end_num_lst, a)


    # 2. end_num_lst에 있는 것 넣기
    elif min_num == min_end_num:
        result.append(min_end_num)
        heapq.heappop(end_num_lst)

    # 3. 둘 다 아닌 것 넣기
    elif min_num == min_basic_num:
        result.append(min_basic_num)
        heapq.heappop(basic_num_lst)


n_result = []
for r in result:
    n_result.append(str(r))
answer = ' '.join(n_result)
print(answer)