N = int(input())

# 소수 리스트 만들기
prime_list = []

def is_prime(num):
    last = int(num ** (1/2))
    result = True
    
    for l in range(2, last + 1):
        if num % l == 0:
            result = False
            break
        
    return result


for i in range(2, N+1):
    if is_prime(i) == True:
        prime_list.append(i)


# 합 이중리스트 만들기
M = len(prime_list)
answer = 0

for b in range(0, M):
    total = 0
    for c in range(b, M):
        total += prime_list[c]
        if total == N:
            answer += 1
            break
        if total > N:
            break

print(answer)
