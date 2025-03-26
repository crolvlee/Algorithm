# 입력받기
N, B = map(int, input().split())
table = []

for _ in range(N):
    line = list(map(int, input().split()))
    table.append(line)

# 행렬곱하는 함수
def operation(X, Y, N):
    result = []
    
    for i in range(0, N):
        row = []
        X_line = X[i]
        
        for j in range(0, N):
            Y_line = []
            for k in range(0, N):
                Y_line.append(Y[k][j])
            
            num = 0
            for m in range(0, N):
                num += (X_line[m] * Y_line[m])
            
            if num != 1000:
                row.append(num % 1000)
            else:
                row.append(num)
        result.append(row)
    
    return result


# 분할 정복
def recursion(table, B):
    if B == 1:
        return table
    
    if B % 2 == 0:
        new_table = recursion(table, B // 2)
        result = operation(new_table, new_table, N)
        return result

    elif B % 2 == 1:
        new_table = recursion(table, B // 2)
        tmp = operation(new_table, new_table, N)
        result = operation(tmp, table, N)
        return result
        
    return result


# 출력
final = recursion(table, B)
for j in range(N):
    line = final[j]
    new_line = []

    for num in line:
        new_num = num % 1000
        new_line.append(str(new_num))

    print(" ".join(new_line))
