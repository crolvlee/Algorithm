def solution(k, tangerine):
    t_dict = {}
    
    for t in tangerine:
        if t not in t_dict:
            t_dict[t] = 1
        else:
            t_dict[t] += 1
    
    t_dict_sorted = sorted(t_dict.items(), key=lambda x: x[1])
    
    cnt = 0         # 제외한 귤의 개수
    kind_cnt = len(t_dict_sorted)   # 선택한 귤의 종류
    for t in t_dict_sorted:
        now_cnt = t[1]
        
        if cnt + now_cnt < len(tangerine) - k:
            kind_cnt -= 1
            cnt += now_cnt
        elif cnt + now_cnt == len(tangerine) - k:
            kind_cnt -= 1
            break
        else:
            break
    
    answer = kind_cnt
    return answer