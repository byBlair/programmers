def solution(n):
    answer = [int(digit) for digit in str(n)]
    answer.sort(reverse=True)
    answer2 = int(''.join(map(str,answer)))
    return answer2