from itertools import combinations

def solution(orders, course):
    combi_dict = {}
    
    for order in orders:
        order = list(order)
        order.sort()
        for i in course:
            combis = combinations(order, i)
            for c in combis:
                if c not in combi_dict:
                    combi_dict[c] = 1
                else:
                    combi_dict[c] += 1
    
    
    combi_list = sorted(combi_dict.items(), key=lambda x: (len(x[0]), -x[1]))
    new_combi_list = []
    
    for combi in combi_list:
        if combi[1] != 1:
            new_combi_list.append(combi)
            
                    
    result = []
    
    # i개의 조합 중에서 value가 가장 큰 것 찾기
    for i in course:
        i_list = []
        max_cnt = 1
        
        for combi in new_combi_list:
            if len(combi[0]) == i:
                if max_cnt < combi[1]:
                    i_list = [combi[0]]
                    max_cnt = combi[1]
                elif max_cnt == combi[1]:
                    i_list.append(combi[0])
            else:
                continue
                
        result += i_list
                
    # 튜플로 되어 있는걸 문자열ㄹ 바꾸기
    answer = []
    for r in result:
        new_str = ''
        for alpha in r:
            new_str += alpha
        answer.append(new_str)
        
    answer.sort()
    
    return answer