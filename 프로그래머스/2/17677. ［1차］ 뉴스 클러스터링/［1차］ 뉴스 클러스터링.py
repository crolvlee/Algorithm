# J(A, B) = n(A^B) / n(aVb)
# A와 B 둘 다 공집합인 경우 -> J(A, B) = 1
 

def solution(str1, str2):
    
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 딕셔너리에 두 글자의 원소를 채워넣기
    str1_dict = {}
    str2_dict = {}
    
    for i in range(len(str1) - 1):
        element = str1[i] + str1[i+1]
        
        if element.isalpha() == False:
            continue
        
        if element in str1_dict:
            str1_dict[element] += 1
        else:
            str1_dict[element] = 1
            
    for j in range(len(str2) - 1):
        element = str2[j] + str2[j+1]
        
        if element.isalpha() == False:
            continue
        
        if element in str2_dict:
            str2_dict[element] += 1
        else:
            str2_dict[element] = 1
    
    # 딕셔너리 2개를 비교하며 합집합, 교집합 찾기
    union_dict = {}
    intersection_dict = {}
    
    # 1. 합집합 찾기
    for k1, v1 in str1_dict.items():
        union_dict[k1] = v1
    
    for k2, v2 in str2_dict.items():
        if k2 not in union_dict:
            union_dict[k2] = v2
        else:
            union_dict[k2] = max(union_dict[k2], v2)
            
    # 2. 교집합 찾기
    for k1, v1 in str1_dict.items():
        if k1 in str2_dict:
            intersection_dict[k1] = min(v1, str2_dict[k1])
        else:
            continue
    
    # 자카드 유사도 구하기
    union_cnt = 0
    intersection_cnt = 0
    
    for ku, vu in union_dict.items():
        union_cnt += vu
    for ki, vi in intersection_dict.items():
        intersection_cnt += vi
    
    if union_cnt == 0:
        jaccard = 1
    else:
        jaccard = intersection_cnt / union_cnt
    
    
    print(union_dict)
    print(intersection_dict)
    print("--------------------")
    print(union_cnt)
    print(intersection_cnt)
    print(jaccard)
    answer = int(jaccard * 65536)
    return answer