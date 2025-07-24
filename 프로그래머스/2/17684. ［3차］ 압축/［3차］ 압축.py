def solution(msg):
    # 딕셔너리 정의
    my_dict = {}
    for i in range(1, 27):
        my_dict[chr(65 + i - 1)] = i
    
    # msg를 처음부터 순회
    answer = []
    idx = 0
    
    while True:
        if idx == len(msg):
            break
        
        # 현재 메시지 시작점에서 뒷 부분 탐색
        now_msg = msg[idx:]
        end_idx = 0
        
        for i in range(0, len(now_msg)):
            if now_msg[:i+1] in my_dict:
                end_idx += 1
            else:
                break
                
        # 현재 입력 w를 answer에 넣기
        w = now_msg[0 : end_idx]
        
        if end_idx < len(now_msg):
            c = now_msg[end_idx]
            my_dict[w + c] = len(my_dict) + 1
            answer.append(my_dict[w])
        else:
            answer.append(my_dict[w])
        
        
        idx += end_idx
        
    
    return answer