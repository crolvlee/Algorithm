# 최소 필요 피로도
# 소모 피로도

from itertools import permutations

def solution(k, dungeons):
    result = permutations(dungeons)
    answer = -1
    
    for r in result:
        now_k = k
        cnt = 0  # 현재 경우에 탐색할 수 있는 최대 던전 수
        for need_score, consume_score in r:
            if now_k >= need_score:
                now_k -= consume_score
                cnt += 1
            else:
                break
        
        answer = max(cnt, answer)
    
    return answer