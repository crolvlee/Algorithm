N = int(input())
lst = list(map(int, input().split()))
result = [1000000000, 1000000000, 1000000000]

lst.sort()
for i in range(0, N-2):
    first_num = lst[i]
    s_idx = i+1
    e_idx = N-1
    
    while True:
        if s_idx == e_idx:
            break
        
        if abs(first_num + lst[s_idx] + lst[e_idx]) < abs(sum(result)):
            result = [first_num, lst[s_idx], lst[e_idx]]
    
        if first_num + lst[s_idx] + lst[e_idx] == 0:
            break
        elif first_num + lst[s_idx] + lst[e_idx] > 0:
            e_idx -= 1
        else:
            s_idx += 1
            

result.sort()
for r in result:
    print(r, end=' ')