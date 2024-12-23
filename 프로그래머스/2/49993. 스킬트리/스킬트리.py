def solution(skill, skill_trees):
    answer = 0
    
    for stree in skill_trees:
        i = 0
        success = True
        for s in stree:
            # 현재 알파벳이 skill에 있다면
            if s in skill:
                if s == skill[i]:
                    i = i+1
                else:
                    success = False
                    break
        if success == True:
            answer += 1

    return answer