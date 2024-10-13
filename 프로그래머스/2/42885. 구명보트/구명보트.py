from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    people = deque(people)
    
    # 배의 개수
    cnt = 0
    
    # [40, 30, 20, 20, 10]
    # [30, 20, 20]
    # [20]
    
    while people:
        if len(people) == 1:
            cnt += 1
            break
        
        elif len(people) >= 2:
            if people[0] + people[-1] <= limit:
                people.pop()    # 인덱스 -1인 원소 pop
            people.popleft()       # 인덱스 0인 원소 pop
            cnt += 1

    
    
    answer = cnt
    return answer