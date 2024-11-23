N, M = map(int, input().split())    # M개를 골라야 함
lst = list(map(int, input().split()))         # 리스트의 길이는 N
result = [[]]

lst.sort()
str_lst = []
for num in lst:
    str_lst.append(str(num))
    

while result and len(result[0]) < M:
    new_result = []
    for r in result:
        for num in str_lst:
            if num in r:
                continue
            new_r = []
            for k in r:
                new_r.append(k)
            new_r.append(num)
            new_result.append(new_r)
    result = []
    for n in new_result:
        result.append(n)

my_str_list = []
for r in result:
    my_str = ''
    for idx in range(len(r)):
        if idx == len(r) - 1:
            my_str += r[idx]
            break
        my_str += r[idx] + ' '
    my_str_list.append(my_str)

for s in my_str_list:
    print(s)