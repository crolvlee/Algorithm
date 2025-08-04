N = int(input())
lst = list(map(int, input().split()))
result = [0]

def binary_search(num):
    s_idx = 0
    e_idx = len(result)
    
    while s_idx <= e_idx:
        m_idx = (s_idx + e_idx) // 2
        if result[m_idx] < num:
            s_idx = m_idx + 1
        else:
            e_idx = m_idx - 1
    
    return s_idx
    

for i in range(0, N):
    if result[-1] < lst[i]:
        result.append(lst[i]) 
    else:
        find_idx = binary_search(lst[i])
        result[find_idx] = lst[i]
        
print(len(result) - 1)