# -1, +1, -10, +10, -100, +100, ...

# 버튼을 누르면 -> (현재 층수 + 버튼 누른 값)의 층으로 이동
# (현재 층수 + 버튼 누른 값) < 0 이면 움직이지 X

# 0층이 가장 아래인 세계관
# 엘레베이터는 현재 민수가 있는 층에 있음

# 마법의 돈 아껴야 함 -> 최소한의 버튼을 눌러서 0층으로 이동해야 함!

# ----
# 1. 현재 자릿값이 6~9 -> 현재 자릿값이 10이 되도록 돌 사용
# 2. 현재 자릿값이 0~4 -> 현재 자릿값이 0이 되도록 돌 사용
# 3. 현재 자릿값이 5
#   3-1. 다음 자릿값이 5~9 -> 현재 자릿값이 10이 되도록 돌 사용
#   3-2. 다음 자릿값이 0~4 -> 현재 자릿값이 0이 되도록 돌 사용

def solution(storey):
    answer = 0
    
    while storey != 0:
        remainder = storey % 10
        
        # 1. 현재 자릿값이 6~9인 경우
        if remainder >= 6:
            rock = 10 - remainder
            storey = (storey + 10) // 10
        
        # 2. 현재 자릿값이 0~4인 경우
        elif remainder <= 4:
            rock = remainder
            storey = storey // 10
            
        # 3. 현재 자릿값이 5인 경우
        elif remainder == 5:
            next_num = (storey // 10) % 10
            
            # 3-1. 다음 자릿값이 5~9인 경우
            if next_num >= 5:
                rock = 10 - remainder
                storey = (storey + 10) // 10
            
            # 3-2. 다음 자릿값이 0~4인 경우
            elif next_num <= 4:
                rock = remainder
                storey = storey // 10
        
        answer += rock
        
    return answer