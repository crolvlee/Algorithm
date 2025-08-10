# 시작 시간은 자정을 넘어가지 않음
# 종료 시간 + 청소시간은 자정을 넘어갈 수도 있음

import heapq

def solution(book_time):
    book_time.sort()
    now_room = []
    
    for s_t, e_t in book_time:
        start_time = int(s_t[0:2]) * 60 + int(s_t[3:5])
        end_time = int(e_t[0:2]) * 60 + int(e_t[3:5])
        if now_room and now_room[0] <= start_time:
            heapq.heappop(now_room)
            heapq.heappush(now_room, end_time + 10)
        else:
            heapq.heappush(now_room, end_time + 10)
    
    answer = len(now_room)
    return answer