N = int(input())
P = list(map(int, input().split()))
P.sort()

store = []
store.append(P[0])

for num in P[1:]:
    new = store[-1] + num
    store.append(new)

print(sum(store))