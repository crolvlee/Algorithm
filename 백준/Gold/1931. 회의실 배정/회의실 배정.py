import sys

N = int(input())
time_list = []

for i in range(N):
    start, end = map(int, input().split())
    time_list.append([start, end])

# end를 기준으로 오름차순 정렬
time_list.sort(key=lambda x:(x[1], x[0]))

selected_meeting_list = []
selected_meeting_list.append([time_list[0][0], time_list[0][1]])

# time_list를 탐색 -> 비교하면서 selected_meeting_list 채워넣기
for tl in time_list[1:]:
    if tl[0] < selected_meeting_list[-1][1]:
        continue
    
    selected_meeting_list.append([tl[0], tl[1]])
    
print(len(selected_meeting_list))