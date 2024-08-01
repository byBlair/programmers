def solution(x):
    answer = sum(int (digit) for digit in str(x))
    if x % answer == 0:
        return True
    else :
        return False
