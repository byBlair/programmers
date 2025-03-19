def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min1 = min(arr)
    return [x for x in arr if x != min1]