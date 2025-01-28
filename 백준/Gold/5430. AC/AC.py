# R 함수: 배열에 있는 수의 순서를 뒤집음
# D 함수: 첫 번째 수를 버림 (배열이 비었는데 사용할 경우, 에러 발생)

from collections import deque

def operation(p, lst):
    lst_q = deque(lst)
    isReversed = 0      # 0 or 짝수인 경우 -> 그대로인 것, 홀수인 경우 -> 뒤집은 것

    # 연산 실행
    for now in p:
        if now == 'R':
            isReversed += 1
        elif now == 'D':
            if len(lst_q) == 0:
                return 'error'

            if isReversed % 2 == 0:     # 리스트가 그대로인 경우
                lst_q.popleft()
            else:                       # 리스트가 뒤집어진 경우
                lst_q.pop()


    result = list(lst_q)
    
    # 남은 것 반환
    if isReversed % 2 == 0:         # 리스트가 그대로인 경우
        return str(result)
    else:                           # 리스트가 뒤집어진 경우
        return str(result[::-1])


T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    lst_input = input()

    if n == 0:
        lst = []
    else:
        lst_input = lst_input[1:-1]
        lst = list(map(int, lst_input.split(",")))

    result = operation(p, lst)
    
    answer = ''
    for r in result:
        if r == ' ':
            continue
        else:
            answer += r
            
    print(answer)