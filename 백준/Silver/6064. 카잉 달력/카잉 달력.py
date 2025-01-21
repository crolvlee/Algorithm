from math import gcd

def find_LCM(a, b):
    return a * b // gcd(a, b)


T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    LCM = find_LCM(M, N)
    answer = -1

    # if M <= N:
    for i in range(x, LCM+1, M):
        if y != N and i % N == y:
            answer = i
            break
        if y == N and i % N == 0:
            answer = i
            break

    print(answer)
