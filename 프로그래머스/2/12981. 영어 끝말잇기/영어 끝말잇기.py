def solution(n, words):
    answer = []
    used = set()
    used.add(words[0])
    for i in range(1, len(words)):
        # 끝말잇기 규칙을 틀렸는지 확인 
        if words[i-1][-1] != words[i][0] :
            return [i % n + 1, i // n + 1]
        # 이미 나온단어인지 확인
        if words[i] in used :
            return [i% n + 1, i // n + 1]
        # 3. 문제 없으면 현재 단어를 저장
        used.add(words[i])
            
    return [0,0]