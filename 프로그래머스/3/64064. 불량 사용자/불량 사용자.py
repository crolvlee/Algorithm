from itertools import permutations

def isMatch(u_id, b_id):
    
    id_length = len(u_id)
    is_match = True
    
    if id_length != len(b_id):
        is_match = False
    else:
        for i in range(id_length):
            if b_id[i] == '*':
                continue
            if b_id[i] == u_id[i]:
                continue
            if b_id[i] != u_id[i]:
                is_match = False
                break
    
    return is_match

    
    
# ====================================
def solution(user_id, banned_id):
    
    select_cnt = len(banned_id)
    perm_list = permutations(user_id, select_cnt)
    
    selected = []
    
    for p in perm_list:
        match_all = True
        for idx in range(select_cnt):
            if isMatch(p[idx], banned_id[idx]) == False:
                match_all = False
                break
        
        if match_all == True:
            p_set = set(p)
            if p_set not in selected:
                selected.append(p_set)
        
    answer = len(selected)
    return answer