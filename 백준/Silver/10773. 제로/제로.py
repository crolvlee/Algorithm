K = int(input())
stack = []

for _ in range(K):

    num = int(input())

    # 현재 수가 0인 경우
    if num == 0:
        if len(stack) == 0:
            stack.append(num)
        else:
            stack.pop()

    # 현재 수가 0이 아닌 경우
    if num != 0:
        stack.append(num)

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))