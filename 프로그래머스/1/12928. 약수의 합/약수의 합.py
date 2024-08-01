def solution(n):
    #약수의 합을 저장할 변수
    sum_of_divisors = 0
    
    # 1부터 n까지의 숫자 중 약수를 찾아 더합니다.
    for i in range(1, n + 1):
        if n % i == 0:
            sum_of_divisors += i
    
    return sum_of_divisors