# progresses: 지금 작업들의 진도
# speeds: 작업 속도

# answer: 각 배포마다 몇 개의 기능이 배포되는지

from collections import deque

def solution(progresses, speeds):
    job_cnt = len(progresses)
    time_q = deque([])
    
    for i in range(job_cnt):
        rest = 100 - progresses[i]
        if rest % speeds[i] == 0:
            time = (rest // speeds[i])
        else:
            time = (rest // speeds[i]) + 1
        time_q.append(time)
        
    # 큐 확인하기
    answer = []
    first_time = time_q.popleft()
    same_cnt = 1
    
    while len(time_q) != 0:
        if time_q[0] <= first_time:
            time_q.popleft()
            same_cnt += 1
        else:
            answer.append(same_cnt)
            first_time = time_q.popleft()
            same_cnt = 1
            
    answer.append(same_cnt)
    return answer