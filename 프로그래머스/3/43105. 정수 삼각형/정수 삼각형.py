# 7
# 3 8
# 8 1 0
# 2 7 4 4


def solution(triangle):
    
    for i, line in enumerate(triangle):
        if i == 0:
            continue
            
        for j in range(len(line)):
            if j == 0:
                line[0] += triangle[i-1][0]
                continue
            if j == i:
                line[j] += triangle[i-1][j-1]
                continue
            
            line[j] += max(triangle[i-1][j-1], triangle[i-1][j])
            
            
    
    answer = max(triangle[-1])
    return answer