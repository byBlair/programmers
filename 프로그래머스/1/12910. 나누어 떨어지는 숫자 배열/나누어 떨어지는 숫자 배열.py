def solution(arr, divisor):
    result = sorted([i for i in arr if i % divisor == 0])
    return result if result else [-1]