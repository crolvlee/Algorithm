N = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]
dp = [(0, arr[0])]

def binary_search(target):
    s_idx = 0
    e_idx = len(LIS)
    
    while s_idx < e_idx:
        m_idx = (s_idx + e_idx) // 2
        if LIS[m_idx] < target:
            s_idx = m_idx + 1
        else:
            e_idx = m_idx
    
    return s_idx

# LIS 만들기
for i in range(1, N):
    if LIS[-1] < arr[i]:
        LIS.append(arr[i])
        dp.append((len(LIS) - 1, arr[i]))
    else:
        idx = binary_search(arr[i])
        LIS[idx] = arr[i]
        dp.append((idx, arr[i]))


# 역추적
result = []
last_idx = len(LIS) - 1
for i in range(N):
    dp_idx = len(dp) - 1 - i

    if last_idx == dp[dp_idx][0]:
        result.append(dp[dp_idx][1])
        last_idx -= 1


result = result[::-1]
n_result = []
for r in result:
    n_result.append(str(r))

print(len(result))
print(' '.join(n_result))