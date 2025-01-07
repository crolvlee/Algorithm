# 중복되는 원소가 없는 튜플이 주어짐
# 순서 고려

def solution(s):
    # 주어진 문자열을 리스트에 저장하기
    s_list = []
    
    split_s = list(map(str, s[2:-2].split('},{')))
    for x in split_s:
        x_list = list(map(int, x.split(',')))
        x_list.append(len(x_list))  # 길이를 넣어줌(구분용) / 나중에 삭제해줄 것임
        s_list.append(x_list)
            
    # s_list 안의 길이(제일 끝 원소)에 따라 정렬해주기
    s_list.sort(key=lambda y:y[-1])
    
    # 아까 임의로 넣은 구분용 원소는 빼주긱
    for sl in s_list:
        sl.pop(-1)
    
    # result를 구하기
    result = []
    
    for sl in s_list:
        for num in sl:
            if num not in result:
                result.append(num)
                break
    
    return result