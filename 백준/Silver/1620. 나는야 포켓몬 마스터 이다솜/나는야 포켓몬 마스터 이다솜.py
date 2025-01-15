import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())    # N: 포켓몬의 개수, M: 내가 맞춰야하는 문제의 개수

int_key_dict = {}       # ex. {1: "Bulbasaur", 2: "Ivysaur"}
str_key_dict = {}       # ex. {"Bulbasaur": 1, "Ivysaur": 2}

for i in range(N):
    name = input().strip()
    int_key_dict[i+1] = name
    str_key_dict[name] = i+1 
    
for _ in range(M):
    info = input().strip()
    
    if info[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        # 입력받은게 숫자인 경우
        print(int_key_dict[int(info)])
    else:
        # 입력받은게 문자인 경우
        print(str_key_dict[info])