# 병합 정렬 이용


def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        
        # 재귀적으로 정렬
        merge_sort(left)
        merge_sort(right)
        
        left_idx, right_idx, merge_idx = 0, 0, 0
        
        # left와 right를 비교하여 병합
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] + right[right_idx] > right[right_idx] + left[left_idx]:
                lst[merge_idx] = left[left_idx]
                left_idx += 1
            else:
                lst[merge_idx] = right[right_idx]
                right_idx += 1
            
            merge_idx += 1
            
        # left나 right에 남은 원소가 있는 경우 (참고: 여기까지 오면 둘 중 하나만 원소 남음)
        while left_idx < len(left):
            lst[merge_idx] = left[left_idx]
            left_idx += 1
            merge_idx += 1
        while right_idx < len(right):
            lst[merge_idx] = right[right_idx]
            right_idx += 1
            merge_idx += 1

def solution(numbers):
    
    new_lst = []
    for num in numbers:
        new_lst.append(str(num))
    
    # 병합 정렬
    merge_sort(new_lst)
    
    answer = ''
    for n in new_lst:
        answer += n
    
    if answer[0] == '0':
        answer = '0'
    
    return answer


# 기댓값:	"1111111101011010010000"
# 결괏값:  "1111111011011010010000"

