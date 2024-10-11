# 잃어버린 괄호

# -가 한 개인 경우: - 바로 뒤부터 끝까지 괄호 안에 넣어주면 됨
# -가 두 개 이상인 경우: -와 - 사이를 괄호에 넣어주면 됨


form = input()
lst = form.split('-')

cal_lst = []
for i, k in enumerate(lst):
    if i == 0:
        num = list(map(int, k.split('+')))
        cal_lst.append(sum(num))
        continue
    else:
        if '+' not in k:
            cal_lst.append(-int(k))
        else:
            num = list(map(int, k.split('+')))
            cal_lst.append(-sum(num))
        
print(sum(cal_lst))