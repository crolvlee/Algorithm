# 백트래킹 문제

def check_new_diagonal(selected_pos, new_row, new_col, N):
    isOk = True

    for r, c in selected_pos:
        if abs(new_row - r) == abs(new_col - c):
            isOk = False
            break
    
    return isOk


# selected_pos에는 [[행 번호(0), 열 번호], [행 번호(1), 열 번호], ...]
def Recursion(selected_pos, depth, N):
    global answer
    if depth == N:
        answer += 1
        return
    
    # 다음 행에서 가능한 열 찾기
    prev_col_list = []
    available_col_list = []
    
    for s_pos in selected_pos:
        prev_col_list.append(s_pos[1])
        
    for i in range(N):
        if i not in prev_col_list:
            available_col_list.append(i)
            
    # 다음 행에서 추가할 점이 대각선 문제 없는지 확인 후,
    # 가능하다면 다음 depth로 넘어가기
    for available_col in available_col_list:
        new_row = selected_pos[-1][0] + 1
        new_col = available_col
        
        if check_new_diagonal(selected_pos, new_row, new_col, N) == True:
            new_selected_pos = selected_pos + [[new_row, new_col]]
            Recursion(new_selected_pos, depth + 1, N)


# 입력받기
N = int(input())

# 백트래킹 실행
answer = 0
for i in range(N):
    Recursion([[0, i]], 1, N)

print(answer)