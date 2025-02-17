# 공평하게 나뉘지 않을 수도 있음!
   

def solution(topping):
    left = set()
    right = {}
    cnt = 0
    
    for t in topping:
        if t not in right:
            right[t] = 1
        else:
            right[t] += 1
    
    for idx, t in enumerate(topping):
        left.add(t)
        
        right[t] = right[t] - 1
            
        # 업데이트 해서 0 되면 -> 그 key는 지우기
        if right[t] == 0:
            del right[t]
        
        if len(left) == len(right):
            cnt += 1
        
        
    return cnt


