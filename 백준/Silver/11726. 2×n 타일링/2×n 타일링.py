# 팩토리얼 함수
def factorial(num):
    result = 1
    if num == 0:
        return result
    else:
        while num != 1:
            result *= num
            num -= 1
        return result

# 입력받기
n = int(input())

# 순회하는 횟수
m = (n // 2) + 1

# 게산
answer = 0

for i in range(m):
    ga_cnt = i * 2
    se_cnt = n - ga_cnt
    
    a = ga_cnt // 2
    b = se_cnt 
    
    comb = factorial(a + b) // (factorial(a) * factorial(b))
    answer = (answer + comb) % 10007
    
print(answer)