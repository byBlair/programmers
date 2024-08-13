def solution(s):
    # 길이가 4 또는 6인지 확인
    if len(s) == 4 or len(s) == 6:
        # 문자열이 숫자로만 구성되어 있는지 확인
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False