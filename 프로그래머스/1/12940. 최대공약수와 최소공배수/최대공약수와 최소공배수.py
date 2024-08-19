import math
def solution(n, m):
    answer = math.gcd(n,m)
    value = abs(n * m) //answer
    return answer,value