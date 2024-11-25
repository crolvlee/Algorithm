# k: 사과의 최대 점수
# m: 한 상자에 넣는 사과의 개수


def solution(k, m, score):
    box_cnt = len(score) // m
    rest_cnt = len(score) % m
    
    score.sort()
    new_score = score[rest_cnt:]

    small_sum = 0
    for i in range(len(new_score)):
        if i % m == 0:
            small_sum += new_score[i]
        
    
    answer = small_sum * m
    return answer