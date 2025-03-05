# [작업의 소요 시간, 작업의 요청 시각, 작업의 번호]   
# 3개 다 작은게 우선순위 높음
# 한 번 작업을 시작하면 마칠 때까지 그것만

import heapq

def solution(jobs):
    q = []
    
    max_time = 0
    for j in jobs:
        max_time += j[1]
        
    jobs.sort()
    
    # 시간 흐르면서 작업 수행
    idx = 0
    is_working = False
    now_job = []    # [작업의 소요 시간, 작업의 요청 시각, 작업의 번호]   
    now_job_end_time = 0
    
    ended_job_cnt = 0
    time = 0
    answer = 0
    
    while True:
        
        if ended_job_cnt == len(jobs):
            break
        
        # 1. 현재 시각에 요청하는 작업이 있는 경우
        while idx < len(jobs) and jobs[idx][0] == time:
            heapq.heappush(q, [jobs[idx][1], jobs[idx][0], idx])
            idx += 1
            
        
        # 2-1. 현재 시각에 종료되는 작업이 있는 경우
        if is_working == True and now_job_end_time == time:
            answer += (now_job_end_time - now_job[1])
            ended_job_cnt += 1
            # 대기큐에 뭔가 있는 경우
            if len(q) > 0:
                next_job = heapq.heappop(q)
                now_job = next_job[:]
                now_job_end_time = time + now_job[0]
                is_working = True
                
            # 대기큐에 아무것도 없는 경우
            else:
                is_working =  False
                now_job = []
                now_job_end_time = 0
        
        # 2-2. 현재 작업을 안 하는 중이고, 대기큐에 뭔가 있다면
        elif is_working == False and len(q) > 0:
            next_job = heapq.heappop(q)
            now_job = next_job[:]
            now_job_end_time = time + now_job[0]
            is_working = True
        
        time += 1

    return answer // len(jobs)