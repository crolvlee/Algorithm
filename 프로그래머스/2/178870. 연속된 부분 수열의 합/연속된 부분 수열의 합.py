def solution(sequence, k):
    left = 0
    right = 0
    answer = [0, len(sequence)-1]
    current_sum = sequence[0]
    
    while True:
        # k보다 작은 경우
        if current_sum < k:
            right += 1
            if right == len(sequence):
                break
            current_sum += sequence[right]
            
        # k와 같은 경우
        elif current_sum == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
                
            current_sum -= sequence[left]
            left += 1
            
            
        # k보다 큰 경우
        else:
            current_sum -= sequence[left]
            left += 1

    return answer