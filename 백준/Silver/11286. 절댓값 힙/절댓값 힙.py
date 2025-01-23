import heapq

my_list = []
heapq.heapify(my_list)

N = int(input())

for _ in range(N):
    current_number = int(input())
    
    if current_number != 0:
        if current_number < 0:
            heapq.heappush(my_list, [-current_number, current_number])
        else:
            heapq.heappush(my_list, [current_number, current_number])
    elif current_number == 0:
        if my_list:
            front = heapq.heappop(my_list)
            print(front[1])
        else:
            print(0)
    