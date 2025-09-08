N = int(input())
lst = list(map(int, input().split()))
set_lst = set(lst)

max_num = max(lst)
score_list = [0] * (max_num + 1)

for a in lst:
    # a의 배수인 것 찾기
    for b in range(a*2, max_num + 1, a):
        if b in set_lst:
            score_list[a] += 1
            score_list[b] -= 1

for num in lst:
    print(score_list[num], end=" ")
