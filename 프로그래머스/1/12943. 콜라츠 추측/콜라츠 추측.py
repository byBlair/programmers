def solution(num):
    answer = 0
    while num != 1: #1이 될때까지 연산해야하므로 while 문 사용
        if num % 2 == 0 :
            num //= 2
        else :
            num = num * 3 + 1
        answer += 1
        
        if answer == 500:
            return -1
        
    return answer 