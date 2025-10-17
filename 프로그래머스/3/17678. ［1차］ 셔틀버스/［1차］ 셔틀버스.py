def solution(n, t, m, timetable):
    
    # 1. 새로운 타임테이블 만들기
    new_timetable = []
    
    for time in timetable:
        hour, minute = time.split(":")
        new_time = int(hour) * 60 + int(minute)
        new_timetable.append(new_time)
        
    new_timetable.sort()
    
    # 2. 셔틀의 타임테이블 만들기
    shuttle_dict = {}
    shuttle_lst = []
    
    for i in range(n):
        shuttle_time = 540 + (t * i)
        
        shuttle_dict[shuttle_time] = []
        shuttle_lst.append(shuttle_time)

    # 3. 기존 크루들이 타는 버스
    crew_idx = 0  # 버스 탈지 확인해야 하는 크루인덱스
    
    for now_shuttle_time in shuttle_lst:
        cnt = 0
        
        while True:
            if cnt == m or crew_idx == len(new_timetable):
                break
            
            if new_timetable[crew_idx] <= now_shuttle_time:
                shuttle_dict[now_shuttle_time].append(new_timetable[crew_idx])
                cnt += 1
                crew_idx += 1
            else:
                break
    
    # 4. 마지막 버스 확인
    last_bus_time = shuttle_lst[-1]
    last_bus_crew_lst = shuttle_dict[last_bus_time][:]
    
    if len(last_bus_crew_lst) < m:
        result = last_bus_time
    else:
        result = max(last_bus_crew_lst) - 1
    
    # 5. 답으로 변환
    result_hour = result // 60
    result_minute = result - result_hour * 60
          
    answer = ''
    
    if result_hour <= 9:
        answer += '0' + str(result_hour)
    else:
        answer += str(result_hour)
        
    answer += ':'
    if result_minute <= 9:
        answer += '0' + str(result_minute)
    else:
        answer += str(result_minute)
    
    return answer