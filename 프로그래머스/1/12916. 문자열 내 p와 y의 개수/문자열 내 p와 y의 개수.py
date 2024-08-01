def solution(s):
    s = s.lower()
    # 'p'와 'y'의 개수를 세기
    p_count = s.count('p')
    y_count = s.count('y')
    
    # 'p'와 'y'의 개수가 같으면 True, 다르면 False 반환
    return p_count == y_count
