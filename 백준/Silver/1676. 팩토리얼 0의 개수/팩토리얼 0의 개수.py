def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return factorial(num - 1) * num

N = int(input())
result = str(factorial(N))

answer = 0

for i in range(len(result), 0, -1):
    if result[i-1] == '0':
        answer += 1
    else:
        break
    
print(answer)