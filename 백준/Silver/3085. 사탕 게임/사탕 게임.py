# 바꿨을 때 영향받는건 세 줄

# 입력받기
N = int(input())
table = []
for _ in range(N):
    line = list(map(str, input()))
    table.append(line)

def count_candy(line):  # line = ['C', 'C', 'P']
    continue_cnt_list = []
    
    record_color = line[0]
    current_cnt = 1
    
    for now_color in line[1:]:
        if now_color == record_color:
            current_cnt += 1
        else:
            continue_cnt_list.append(current_cnt)
            record_color = now_color
            current_cnt = 1
            
    continue_cnt_list.append(current_cnt)
    return max(continue_cnt_list)

#===============================
# 바꾸기 전, 행별 최대 연속되는 수
row_max_list = []
for row in table:
    row_max = count_candy(row)
    row_max_list.append(row_max)

# 바꾸기 전, 열별 최대 연속되는 수
col_max_list = []
for i in range(0, N):
    col_line = []   # i열에 해당하는 것들
    for j in range(0, N):
        col_line.append(table[j][i])
    col_max = count_candy(col_line)
    col_max_list.append(col_max)
    
#===============================
# 바꿨을 때의 최댓값
affect_max_list = []

# 가로로 쭉 (같은 행의 x열과 x+1열이 자리를 바꿈)
for r in range(0, N):
    for c in range(0, N-1):
        if table[r][c] != table[r][c+1]:
            table[r][c], table[r][c+1] = table[r][c+1], table[r][c] # 이거 뒤에 원위치 시켜줄거임
            
            # 영향받는 현재 r행
            line1 = table[r]
            line1_max_candy = count_candy(line1)
            affect_row_max = max(row_max_list[:r] + [line1_max_candy] + row_max_list[r+1:])
            
            # 영향받는 c열
            line2 = []
            for i in range(0, N):
                line2.append(table[i][c])
            line2_max_candy = count_candy(line2)
            
            # 영향받는 c+1열
            line3 = []
            for i in range(0, N):
                line3.append(table[i][c+1])
            line3_max_candy = count_candy(line3)

            affect_col_max = max(col_max_list[:c] + [line2_max_candy, line3_max_candy] + col_max_list[c+2:])
            
            affect_max = max(affect_row_max, affect_col_max)
            affect_max_list.append(affect_max)
            
            table[r][c], table[r][c+1] = table[r][c+1], table[r][c] # 바꾼거 원위치
        else:
            continue
        


# 세로로 쭉 (같은 열의 x행과 x+1행이 서로 자리를 바꿈)
for c in range(0, N):
    for r in range(0, N-1):
        if table[r][c] != table[r+1][c]:
            table[r][c], table[r+1][c] = table[r+1][c], table[r][c]
            
            # 영향받는 현재 c열
            line1 = []
            for i in range(N):
                line1.append(table[i][c])
            line1_max_candy = count_candy(line1)
            
            affect_col_max = max(col_max_list[:c] + [line1_max_candy] + col_max_list[c+1:])
            
            # 영향받는 r행
            line2 = table[r]
            line2_max_candy = count_candy(line2)
            
            # 영향받는 r+1행
            line3 = table[r+1]
            line3_max_candy = count_candy(line3)
            
            affect_row_max = max(row_max_list[:r] + [line2_max_candy, line3_max_candy] + row_max_list[r+2:])
            
            affect_max = max(affect_row_max, affect_col_max)
            affect_max_list.append(affect_max)
            
            table[r][c], table[r+1][c] = table[r+1][c], table[r][c]
        else:
            continue

print(max(affect_max_list))