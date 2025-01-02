# 입력받기
N = int(input())
tanghuru = list(map(int, input().split()))

start = 0
fruit_count = {}
max_fruit = 0

# 과일 종류 개수 함수 정의
def count_kind(lst):
    record = []
    for num in lst:
        if num not in record:
            record.append(num)
    
    return len(record)

for end in range(0, N):
    # 현재 과일 추가
    if tanghuru[end] in fruit_count:
        fruit_count[tanghuru[end]] += 1
    else:
        fruit_count[tanghuru[end]] = 1
        
    # 과일 종류가 두 종류를 초과하면 -> start 포인터 이동
    if len(fruit_count) > 2:
        fruit_count[tanghuru[start]] -= 1
        if fruit_count[tanghuru[start]] == 0:
            del fruit_count[tanghuru[start]]
        start += 1
    
    # 남은 과일 수 갱신
    max_fruit = max(max_fruit, end - start + 1)    

print(max_fruit)