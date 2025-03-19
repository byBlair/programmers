def solution(numbers):
    answer = 0
    all = [0,1,2,3,4,5,6,7,8,9]
    for i in all:
        if i not in numbers:
            answer += i
    return answer