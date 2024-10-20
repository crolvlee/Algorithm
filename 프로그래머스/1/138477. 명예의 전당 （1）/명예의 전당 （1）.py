def solution(k, score):
    
    honor = []      # 명예의 전당
    result = []     # 발표점수
    
    for s in score:
        # honor의 수가 k보다 작은 경우
        if len(honor) < k:
            honor.append(s)
            honor.sort()
            result.append(honor[0])
            continue
        
        # honor에 있는 것과 현재 s 비교
        # honor의 최소보다 현재 s가 크다면 -> s를 honor에 추가
        if honor[0] < s:
            honor.pop(0)
            honor.append(s)
            honor.sort()
            
        result.append(min(honor))
                

    return result