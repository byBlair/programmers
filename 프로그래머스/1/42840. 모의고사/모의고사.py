def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    # 수포자들의 점수를 저장할 리스트
    
   # 각 수포자의 패턴과 정답이 얼마나 일치하는지 확인 
    scores =[0] * 3
    for i,answer in enumerate(answers):
        for j,pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    # 가장 높은 점수 저장
    max_score = max(scores)
    
    high=[]
    for i,score in enumerate(scores):
        if score == max_score:
            high.append(i + 1)
    return high