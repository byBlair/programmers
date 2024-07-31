def solution(a, b): 
    ab = int(str(a) + str(b))
    
    # 2 * a * b를 계산
    ab2 = 2 * a * b
    
    # 두 값을 비교하여 더 큰 값을 반환, 같으면 ab를 반환
    if ab >= ab2:
        return ab
    else:
        return ab2