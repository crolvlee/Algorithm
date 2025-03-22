first_str = input()
explosion_str = input()

stack = []

for i in range(len(first_str)):
    stack.append(first_str[i])
    if len(stack) >= len(explosion_str):
        if ''.join(stack[-len(explosion_str):]) == explosion_str:
            for j in range(len(explosion_str)):
                stack.pop()


if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))