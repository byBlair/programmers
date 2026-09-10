def solution(s):
    answer = []
    last = {}
    for i in range(len(s)):
        if s[i] not in last:
            answer.append(-1)
        else :
            answer.append(i - last[s[i]])
        last[s[i]] = i
    return answer
        