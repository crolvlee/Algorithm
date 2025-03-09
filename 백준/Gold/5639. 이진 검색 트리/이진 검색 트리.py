import sys
sys.setrecursionlimit(20000)

lst = []

while True:
    try:
        num = int(input())
        lst.append(num)
    except:
        break
    
def post_order(lst):
    if len(lst)  == 0:
        return
    
    tempL = []
    tempR = []
    
    now  = lst[0]
    found = False   # now 뒤에 now보다 큰 숫자 찾음
    for i in range(1, len(lst)):
        if lst[i] > now:
            tempL = lst[1:i]
            tempR = lst[i:]
            found = True
            break
    
    # now뒤에 다 작은 숫자만 있다면
    if found == False:
        tempL = lst[1:]
        tempR = []
    
    post_order(tempL)
    post_order(tempR)
    print(now)
    
post_order(lst)