N = int(input())
x_list = []
y_list = []

for _ in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_list.append(x_list[0])
y_list.append(y_list[0])

# 신발끈 공식 이용
a = 0
for i in range(0, N):
    x_now = x_list[i]
    y_now = y_list[i + 1]
    a += (x_now * y_now)

b = 0
for i in range(1, N+1):
    x_now = x_list[i]
    y_now = y_list[i-1]
    b += (x_now * y_now)

result = abs(a - b) * (1 / 2)
print(round(result, 1))
