from collections import deque

N = int(input())
lst = deque([])
for i in range(1, N+1):
    lst.append(i)
    
while len(lst) != 1:
    lst.popleft()
    a = lst.popleft()
    lst.append(a)
    
print(lst[0])