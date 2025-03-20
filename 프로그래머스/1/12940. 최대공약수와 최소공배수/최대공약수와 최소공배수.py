import math
def solution(n, m):
    answer = math.gcd(n,m)
    answer2 = abs(n * m) // math.gcd(n,m)
    return answer,answer2