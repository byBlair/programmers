def solution(participant, completion):
    answer = {}
    #먼저 참가자들 갯수를 세고
    for i in participant:
        if i in answer :
            answer[i] += 1
        else:
            answer[i] = 1
    # 딕셔너리에 1 저장 되어 있는거라 0이 나오는애들이 있겠지?
    for i in completion:
        answer[i] -= 1
    #그리고 또 포문을 돌면서 i보다 작은 애를 반환
    for i in answer :
        if answer[i] > 0:
            return i