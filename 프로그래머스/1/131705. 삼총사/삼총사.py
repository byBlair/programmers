from itertools import combinations
def solution(number):
    answer = 0
    for i in combinations(number, 3): #3개씩 조합
        if sum(i) == 0:
            answer += 1
    return answer