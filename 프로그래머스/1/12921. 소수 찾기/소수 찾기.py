def solution(n):
    answer = 0
    for i in range(2, n + 1):
        is_P = True
        
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0 :
                is_P = False
                break
                
        if is_P:        
            answer +=1
    return answer