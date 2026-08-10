def solution(X, Y):
    dic_X = {}
    dic_Y = {}
    
    # X 숫자 세기
    for i in X:
        if i in dic_X:
            dic_X[i] += 1
        else:
            dic_X[i] = 1
    # Y 숫자 세기
    for i in Y:
        if i in dic_Y:
            dic_Y[i] += 1
        else:
            dic_Y[i] = 1
    # 공통 숫자 담기
    answer = []
    for i in dic_X:
        if i in dic_Y:
            count = min(dic_X[i], dic_Y[i])
            for _ in range(count):
                answer.append(i)
    answer.sort(reverse= True)
    
    #공통숫자 없으면
    if not answer:
        return "-1"
    if answer[0] == "0":
        return "0"
    
    return "".join(answer)
            