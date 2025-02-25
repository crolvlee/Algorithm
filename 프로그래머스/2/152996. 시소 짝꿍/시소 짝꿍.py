# 1:1
# 1:2
# 2:3
# 3:4

def solution(weights):
    weights_dict = {}
    
    for w in weights:
        if w not in weights_dict:
            weights_dict[w] = 1
        else:
            weights_dict[w] += 1
            
    # 현재 w에 대응이 가능한, weight보다 크거나 같은 숫자를 찾음
    answer = 0
    
    for weight, weight_cnt in weights_dict.items():
        
        # 1:1 (현재 weight가 여러 개 있을 경우)
        if weight_cnt > 1:
            answer += (weight_cnt * (weight_cnt - 1)) / 2
        # 1:2 
        if weight * 2 in weights_dict:
            answer += weight_cnt * weights_dict[weight * 2]
        # 2:3
        if (weight * 3) / 2 in weights_dict:
            answer += weight_cnt * weights_dict[(weight * 3) / 2]
        # 3:4
        if (weight * 4) / 3 in weights_dict:
            answer += weight_cnt * weights_dict[(weight * 4) / 3]
        
    return answer