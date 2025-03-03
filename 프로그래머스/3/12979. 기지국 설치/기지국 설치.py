# n: 아파트의 개수
# stations: 이미 설치되어 있는 4g 기지국의 번호
# w: 전파의 도달거리


def solution(n, stations, w):
    
    # 회색 아파트 그룹 찾기
    group_cnt_list = []
    group_start = 1
    
    for station in stations:
        # 현재 station 바로 전의 회색그룹 구하기
        group_end = station - w - 1
        group_cnt = group_end - group_start + 1
        group_cnt_list.append(group_cnt)
        
        # 다음으로
        group_start = station + w + 1
        
    # 마지막 회색 그룹이 남아 있는 경우
    if group_start <= n:
        last_group_cnt = n - group_start + 1
        group_cnt_list.append(last_group_cnt)
    
    
    # 각 회색 그룹별 필요한 기지국의 개수 구하기
    answer = 0
    
    for gc in group_cnt_list:
        # 하나의 5g 기지국이 영향을 미치는 범위
        effect = 2*w + 1
        
        # 필요한 5g 기지국
        if gc % effect == 0:
            new_5g_cnt = gc // effect
        else:
            new_5g_cnt = (gc // effect) + 1
            
        answer += new_5g_cnt
    
    
    return answer