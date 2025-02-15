N = int(input())

num_list = []

for _ in range(N):
    x, y = map(int, input().split())
    num_list.append([x, y])
    
num_list.sort(key=lambda x: (x[1], x[0]))

for num in num_list:
    print(num[0], num[1])