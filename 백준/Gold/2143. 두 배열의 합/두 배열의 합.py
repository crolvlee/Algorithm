# 입력받기
T = int(input())
n = int(input())
A_list = list(map(int, input().split()))
m = int(input())
B_list = list(map(int, input().split()))

# A_list와 B_list의 부분합 구하기
A_sum = []
B_sum = []

for i in range(0, n):
    for j in range(i, n):
        A_sum.append(sum(A_list[i:j+1]))

for i in range(0, m):
    for j in range(i, m):
        B_sum.append(sum(B_list[i:j+1]))

# 부분합 정렬
A_sum.sort()
B_sum.sort()

# 특정 값의 시작 인덱스 찾는 함수
def lower_bound(lst, target):
    s_idx = 0
    e_idx = len(lst)
    
    while s_idx < e_idx:
        m_idx = (s_idx + e_idx) // 2
        
        if lst[m_idx] < target:
            s_idx = m_idx + 1
        else:
            e_idx = m_idx
            
    return s_idx        

# 특정 값의 끝 인덱스 찾는 함수
def upper_bound(lst, target):
    s_idx = 0
    e_idx = len(lst)

    while s_idx < e_idx:
        m_idx = (s_idx + e_idx) // 2

        if lst[m_idx] <= target:
            s_idx = m_idx + 1
        else:
            e_idx = m_idx

    return s_idx

# A_sum 중 특정 원소 + B_sum 중 특정 원소 = T인 것 찾기
answer = 0

for a in A_sum:
    num = T - a
    
    start_idx = lower_bound(B_sum, num)
    end_idx = upper_bound(B_sum, num)
    cnt = end_idx - start_idx
    answer += cnt
    
print(answer)