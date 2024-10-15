# 1번 -> 1, 2, 3, 4, 5
# 2번 -> 2, 1, 2, 3, 2, 4, 2, 5
# 3번 -> 3, 3, 1, 1, 2, 2, 4, 4, 5, 5


def solution(answers):
    
    stu1 = [1, 2, 3, 4, 5]
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    # 1번 수포자
    for i, answer in enumerate(answers):
        idx = i % 5
        if stu1[idx] == answer:
            score1 += 1
    
    # 2번 수포자
    for i, answer in enumerate(answers):
        idx = i % 8
        if stu2[idx] == answer:
            score2 += 1    
            
    # 3번 수포자
    for i, answer in enumerate(answers):
        idx = i % 10
        if stu3[idx] == answer:
            score3 += 1
    
    max_student_num = []
    max_score = max(score1, score2, score3)
    if max_score == score1:
        max_student_num.append(1)
    if max_score == score2:
        max_student_num.append(2)
    if max_score == score3:
        max_student_num.append(3)
    
    return max_student_num