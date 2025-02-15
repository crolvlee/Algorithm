# 비밀번호 찾기


import sys
# sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N: 저장된 사이트 주소의 수
# M: 비밀번호를 찾으려는 사이트 주소의 수
N, M = map(int, input().split())

# 이메일, 비밀번호 저장하기
store = {}
for _ in range(N):
    email, password = map(str, input().split())
    store[email] = password
    

for _ in range(M):
    email = str(input()).strip()
    print(store[email])
    