import sys
input = sys.stdin.readline

N = int(input())
min_previous = []
max_previous = []

for i in range(N):
    if i == 0:
        line = list(map(int, input().split()))
        min_previous = line
        max_previous = line
    else:
        line = list(map(int, input().split()))

        min_first = min(line[0] + min_previous[0], line[0] + min_previous[1])
        min_second = min(line[1] + min_previous[0], line[1] + min_previous[1], line[1] + min_previous[2])
        min_third = min(line[2] + min_previous[1], line[2] + min_previous[2])
        min_previous = [min_first, min_second, min_third]

        max_first = max(line[0] + max_previous[0], line[0] + max_previous[1])
        max_second = max(line[1] + max_previous[0], line[1] + max_previous[1], line[1] + max_previous[2])
        max_third = max(line[2] + max_previous[1], line[2] + max_previous[2])
        max_previous = [max_first, max_second, max_third]


min_result = min(min_previous)
max_result = max(max_previous)

print(max_result, min_result)
