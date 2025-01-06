# 다 길이만큼 돌긴 함. but 중복되는 수는 제거하기

# 1개 뽑기

# 2개 뽑개
# 7 + 9 = 16            # 첫 원소의 인덱스가 0
# 16 - 7 + 1 = 10       # 첫 원소의 인덱스가 1 (기존합 - 인덱스0 원소 + 인덱스2 원소)
# 10 - 9 + 1 = 2        # 첫 원소의 인덱스가 2 (기존합 - 인덱스1 원소 + 인덱스3 원소)
# 2 - 1 + 4 = 5         # 첫 원소의 인덱스가 3 (기존합 - 인덱스2 원소 + 인덱스4 원소)
# 5 - 1 + 7 = 11        # 첫 원소의 인덱스가 4 (기존합 - 인덱스3 원소 + 인덱스0 원소)

# 3개 뽑기
# 7 + 9 + 1 = 17        # 첫 원소의 인덱스가 0
# 17 - 7 + 1 = 11       # 첫 원소의 인덱스가 1 (기존합 - 인덱스0 원소 + 인덱스3 원소)
# 11 - 9 + 4 = 6        # 첫 원소의 인덱스가 2 (기존합 - 인덱스1 원소 + 인덱스4 원소)
# 6 - 1 + 7 = 12        # 첫 원소의 인덱스가 3 (기존합 - 인덱스2 원소 + 인덱스0 원소)
# 12 - 1 + 9 = 20       # 첫 원소의 인덱스가 4 (기존합 - 인덱스3 원소 + 인덱스1 원소)




def solution(elements):
    result = []
    
    for i in range(len(elements)):  # i는 뽑는 부분수열의 길이 - 1
        hab_list = []       # [16, 10, 2, 5, 11]
        select_cnt = i+1
        
        # 현재 합 (초기화)
        current_hab = 0
        
        for j in range(0, select_cnt):
            current_hab += elements[j]
        hab_list.append(current_hab)
            
        # 현재 합 (업데이트)
        for k in range(1, len(elements)):  # k는 부분수열의 첫번째 원소의 인덱스
            # 지울 원소의 인덱스
            delete_idx = k-1
            
            # 추가할 원소의 인덱스
            if k + select_cnt - 1 >= len(elements):
                add_idx = (k + select_cnt - 1) - len(elements)
            else:
                add_idx = k + select_cnt - 1
            
            current_hab = current_hab - elements[delete_idx] + elements[add_idx]
            hab_list.append(current_hab)
            
        # hab_list를 result에 넣기
        for h in hab_list:
            result.append(h)
            
    result = set(result)
    answer = len(result)
    return answer