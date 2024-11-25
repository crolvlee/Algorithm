# 시작 시간은 자정을 넘어가지 않음
# 종료 시간 + 청소시간은 자정을 넘어갈 수도 있음

def solution(book_time):
    fill_time = []
    for bt in book_time:
        start_hour, start_min = bt[0].split(':')
        end_hour, end_min = bt[1].split(':')
        
        start = int(start_hour) * 60 + int(start_min)
        end = int(end_hour) * 60 + int(end_min) + 10
        fill_time.append([start, end])
    
    fill_time.sort()
    # print(fill_time)
    
    timeline = []   # [[1, 1160], [2, 920]]
    for ft in fill_time:
        # timeline에 아무것도 없는 경우
        if len(timeline) == 0:
            timeline.append([1, ft[1]])
            continue
            
        # timeline에 뭔가 있는 경우
        enter = False
        for tl in timeline:
            if tl[1] <= ft[0]:
                tl[1] = ft[1]
                enter = True
                break
        if enter == False:
            timeline.append([len(timeline) + 1, ft[1]])
        
        # print("---------")
        # print(timeline)
        
    answer = len(timeline)
    return answer