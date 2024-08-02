def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    total_sum = 0
    for a,b in zip(A,B):
        total_sum += a * b
    return total_sum