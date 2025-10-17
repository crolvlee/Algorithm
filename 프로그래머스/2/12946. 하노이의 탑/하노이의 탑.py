def solution(n):
    answer = []
    
    def hanoi(k, from_pos, to_pos, sub_pos):
        nonlocal answer
        if k == 1:
            answer.append([from_pos, to_pos])
            return
        
        hanoi(k-1, from_pos, sub_pos, to_pos)
        answer.append([from_pos, to_pos])
        hanoi(k-1, sub_pos, to_pos, from_pos)
        
    hanoi(n, 1, 3, 2)
    return answer