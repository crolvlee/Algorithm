T = int(input())
for _ in range(T):
    n = int(input())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    
    dp_first = []
    dp_second = []
    
    for i in range(n):
        if i == 0:
            dp_first.append(first[0])
            dp_second.append(second[0])
        
        elif i == 1:
            dp_first.append(second[0] + first[1])
            dp_second.append(first[0] + second[1])
            
        elif i >= 2:
            first_max = max(dp_second[i-2] + first[i], dp_second[i-1] + first[i])
            second_max = max(dp_first[i-2] + second[i], dp_first[i-1] + second[i])
            dp_first.append(first_max)
            dp_second.append(second_max)
            
    print(max(dp_first[-1], dp_second[-1]))