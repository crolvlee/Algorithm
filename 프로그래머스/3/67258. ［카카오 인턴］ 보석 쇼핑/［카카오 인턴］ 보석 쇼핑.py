# 투 포인터
def solution(gems):
    goal_cnt = len(set(gems))
    start = 0
    end = 0
    index_list = []
    gem_dict = {}
    
    while end < len(gems):
        # 현재 start ~ end에서의 종류를 gem_dict에 넣기
        if gems[end] in gem_dict:
            gem_dict[gems[end]] += 1
        else:
            gem_dict[gems[end]] = 1
        
        # 종류 수가 찾으려는 수인 경우
        if len(gem_dict) == goal_cnt:
            # start를 옮김
            while start <= end:
                if gem_dict[gems[start]] > 1:
                    gem_dict[gems[start]] -= 1
                    start += 1
                else:
                    break
            
            index_list.append([end-start+1, start, end])
            
        end += 1
            
    index_list.sort()

    answer = [index_list[0][1] + 1, index_list[0][2] + 1]
    return answer