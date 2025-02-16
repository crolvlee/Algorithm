# 입력받기
n = int(input())
goal = []

for _ in range(n):
    num = int(input())
    goal.append(num)
    
# 스택에 넣기 (1, 2, 3, 4 ... 순으로)
stack = []
goal_idx = 0
result = []     # '+', '-'가 들어가는 배열

for i in range(1, n+1):
    if goal[goal_idx] != i:
        stack.append(i)
        result.append('+')
    elif goal[goal_idx] == i:
        result.append('+')
        result.append('-')
        goal_idx += 1
        
        # 빼는 while문
        while True:
            if stack and stack[-1] == goal[goal_idx]:
                stack.pop()
                result.append('-')
                goal_idx += 1
            else:
                break
        
if len(stack) > 0:
    print("NO")
else:
    for r in result:
        print(r)