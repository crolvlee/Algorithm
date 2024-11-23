def solution(s, n):
    big = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small = "abcdefghijklmnopqrstuvwxyz"
    new_s = ""
    
    
    
    for current in s:
        # 대문자인 경우
        if current in big:
            idx = big.find(current)
            if idx + n >= len(big):
                new_s += big[n-len(small)+idx]
            else:
                new_s += big[idx + n]
        # 소문자인 경우
        elif current in small:
            idx = small.find(current)
            if idx + n >= len(small):
                new_s += small[n-len(small)+idx]
            else:
                new_s += small[idx+n]
        # 공백인 경우
        else:
            new_s += " "
    
    return new_s