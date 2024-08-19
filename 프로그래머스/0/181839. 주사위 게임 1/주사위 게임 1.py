def solution(a, b):
    answer = 0
    a_odd = a % 2
    b_odd = b % 2
    
    if a_odd == 1 and b_odd ==1:
        answer = a **2 +b**2
    elif a_odd ==1 or b_odd ==1:
        answer = 2*(a+b)
    else:
        answer = abs(a-b)
    return answer