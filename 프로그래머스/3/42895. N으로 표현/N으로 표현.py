def calculate(prev1, prev2):
    result = set()
    
    for p1 in prev1:
        for p2 in prev2:
            a = p1 + p2
            b = p1 * p2
            c = p1 - p2
            d = p1 // p2
            e = p2 - p1
            f = p2 // p1
            
            current = {a, b, c, d, e, f}
            for cur in current:
                if cur >= 1:
                    result.add(cur)
    
    return result
    

def solution(N, number):
    if N == number:
        return 1
    
    dp = {1: {N}}     # dp = {1: {9}, 2: {99, 18, 81, 1}, 3: {}, .....}
    find = False
    answer = -1
    
    # i는 N을 사용한 횟수
    for i in range(2, 9):
        i_set = set()
        i_set.add(int(str(N) * i))
        for j in range(1, i//2 + 1):
            prev1 = dp[j]
            prev2 = dp[i - j]
            
            # 연산 수행
            new_set = calculate(prev1, prev2)
            
            for num in new_set:
                i_set.add(num)

        if number in i_set:
            find = True
            answer = i
            dp[i] = i_set
            break
        else:
            dp[i] = i_set
            
    if answer > 8:
        return -1
    else:
        return answer