# 한 번 증설한 서버는 k시간 동안 운영하고, 그 이후에는 반납됨
# 0*m명 이상 (0+1)*m명 미만 -> 서버 0대 필요
# n*m명 이상 (n+1)*m명 미만 -> 서버 n대 필요

# players: 24시간 동안의 이용자 수
# m: 서버 1대로 감당할 수 있는 최대 이용자의 수
# k: 서버 1대가 운영 가능한 시간

# m = 3일 때
# 0명 이상 ~ 3명 미만 -> 최소 0대의 서버 필요
# 3명 이상 ~ 6명 미만 -> 최소 1대의 서버 필요
# 6명 이상 ~ 9명 미만 -> 최소 2대의 서버 필요

def solution(players, m, k):
    answer = 0
    
    time_server_dict = {}   # 특정 시각에 증설된 서버의 개수를 담음
    for i in range(0, 24):
        time_server_dict[i] = 0
    
    for start_time, player in enumerate(players):
        server_need_cnt = player // m
        server_now_cnt = 0
        
        for j in range(1, k):
            if start_time - j >= 0:
                server_now_cnt += time_server_dict[start_time - j]
            
        if server_need_cnt > server_now_cnt:
            time_server_dict[start_time] = server_need_cnt - server_now_cnt
            answer += server_need_cnt - server_now_cnt
            
    print(time_server_dict)
             
    return answer