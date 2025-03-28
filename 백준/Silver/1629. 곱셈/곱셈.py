A, B, C = map(int, input().split())

def recursion(X):
    if X == 1:
        return A % C

       # 지수가 짝수인 경우
    if X % 2 == 0:
        result = recursion(X//2) 
        return (result * result) % C
    # 지수가 홀수인 경우
    elif X % 2  == 1:
        first = recursion(X//2)
        second = recursion(X//2 + 1) 
        return (first * second) % C

answer = recursion(B)
print(answer)
