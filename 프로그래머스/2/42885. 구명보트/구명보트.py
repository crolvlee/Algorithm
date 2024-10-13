# # 투 포인터

# from collections import deque

# def solution(people, limit):
#     people.sort()   # [50, 50, 70, 80]
    
#     # 현재 보트의 개수
#     boat = 0
    
#     # 투포인터 초기화
#     a = 0
#     b = len(people)-1
    
#     # 현재 보트에 탄 인원의 무게 합
#     current = 0
    
#     # 보트에 태우기
#     while a <= b:
#         if a == b:
#             if current + people[b] <= limit:
#                 boat += 1
#             else:
#                 boat += 2
#             b -= 1
#         else:
#             if current + people[b] <= limit:
#                 current += people[b]
#                 b -= 1
#             elif current + people[a] <= limit:
#                 current += people[a]
#                 a += 1
#             else:
#                 current = 0
#                 boat += 1
        
        
#     answer = boat
#     return answer
def solution(people, limit):
    first = 0
    last = len(people) - 1
    answer = 0

    people.sort(reverse = True)

    while first <= last:

        if people[first] + people[last] <= limit:
            last -= 1

        first += 1
        answer += 1


    return answer