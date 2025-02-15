M, N = map(int, input().split())

# 소수 판별 함수
def check_is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    is_prime = True
    sqrt_root = num ** (0.5)
    
    for i in range(2, int(sqrt_root) + 1):
        if num % i == 0:
            is_prime = False
            break

    return is_prime

for now in range(M, N+1):
    if check_is_prime(now) == True:
        print(now)