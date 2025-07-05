def solution(names):
    answer = []
    for i in range(0, len(names), 5): #5명씩 그룹화
        answer.append(names[i])    
    return answer