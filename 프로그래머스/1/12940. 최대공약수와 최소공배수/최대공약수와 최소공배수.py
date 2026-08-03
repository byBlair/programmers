def solution(n, m):
    a = n
    b = m
    while m != 0 :
        n,m = m, n % m
    lcd = (a * b) // n
    return n, lcd