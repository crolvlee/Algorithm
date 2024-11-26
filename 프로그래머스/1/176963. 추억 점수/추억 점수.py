def solution(name, yearning, photo):
    result = []
    
    for p in photo:
        p_score = 0
        for person in p:
            for idx, n in enumerate(name):
                if n == person:
                    n_score = yearning[idx]
                    p_score += n_score
                    break
        result.append(p_score)
            
    
    return result