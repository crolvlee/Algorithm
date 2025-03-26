N = int(input())
sang_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

sang_dict = {}
for num in sang_list:
    if num not in sang_dict:
        sang_dict[num] = 1
    else:
        sang_dict[num] += 1
        
result = []
for m in M_list:
    if m in sang_dict:
        result.append(str(sang_dict[m]))
    else:
        result.append(str(0))
        
print(" ".join(result))