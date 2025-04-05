T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    line = input()

    # 홀수인 경우
    if N % 2 == 1:
        answer = 0
        print(f"#{test_case} {answer}")

    # 짝수인 경우
    elif N % 2 == 0:
        answer = 0
        stack = []

        for a in line:
            # 여는 괄호인 경우
            if a in ['(', '[', '{', '<']:
                stack.append(a)

            # 닫는 괄호인 경우
            else:
                if a == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        stack.append(a)
                elif a == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        stack.append(a)
                elif a == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(a)
                elif a == '>':
                    if stack and stack[-1] == '<':
                        stack.pop()
                    else:
                        stack.append(a)

        if len(stack) > 0:
            answer = 0
        else:
            answer = 1

        print(f"#{test_case} {answer}")

    # ///////////////////////////////////////////////////////////////////////////////////
